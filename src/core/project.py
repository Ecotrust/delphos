import sqlalchemy
import logging
import os
import sys
import csv
from sqlalchemy import *

from project_data import *
from alternative_set import *
from criteria_set import *
from input_matrix import *
from mca_runs import *
from delphos_exceptions import *
from csv_types import *

#from data import default_criteria
from data.old_india1_criteria import *
from data import default_alternatives
from evamix.evamix import *

class Project:
    """Represents a delphos project.
    
    Provides functionality to maintain a project including alternatives, criteria and multicriteria 
    analysis results.  In most cases GUI widgets should invoke operations through this object instead of accessing
    lower level core objects directly
    """
    
    def __init__(self, name, path, type=None, load_default_altern=False, load_default_crit=False):
        """new_project = Project(string, string, string, boolean, boolean)
        
        Default criteria are a predetermined set of criteria thought to be common to
        projects of a given type.  These criteria are stored on disk.
        """
        self.debug = True
        self.name = name
        self.path = path
        self.type = type    #Fisheries or MPA
        self.db_driver = 'sqlite'
        self.db_file_ext = '.dlp'
        self.status_ok = False     #1-OK, 0-Error
        self.error = ""        #Error message
        
        self.project_table_name = 'project_data'
        self.project_data = None    #General ProjectData
        self.altern_table_name = 'alternatives'
        self.altern_set = None    #Primary AlternativeSet
        self.crit_table_name = 'criteria'
        self.crit_set = None    #Primary CriteriaSet
        self.mca_runs_table_name = 'mca_runs'
        self.mca_runs = None	#Holds analysis runs for project
        self.input_matrix_name = 'input_matrix'
        self.input_matrix = None    #Primary input matrix
        
        if self.type == "fisheries":
            self.default_alternatives = default_alternatives.fisheries_default_alternatives
            self.default_criteria = fisheries_default_criteria
        elif self.type == "mpa":
            self.default_criteria = mpa_default_alternatives
            self.default_criteria = mpa_default_criteria
        
        self.__create_project_db()
        if self.status_ok:
            self.__create_project_data()
            self.__create_alternative_set(load_default_altern)
            self.__create_criteria_set(load_default_crit)
            self.__create_mca_runs_table()
        
    def __create_project_db(self):
        """Creates a persistent DB for storing project data.
        """
        #TODO: catch exception
        db = create_engine(self.db_driver+':///'+self.path+os.sep+self.name)
        self.meta = BoundMetaData(db)            #Basically a schema, or table collection
        if self.debug:
            self.meta.engine.echo = False
        self.status_ok = True

    def __create_project_data(self):
        project_name = self.name[:-4]
        self.project_data = ProjectData(self.meta, self.project_table_name, project_name, self.type)

    def __create_alternative_set(self, load_default_altern=False):
        """Create an AlternativeSet for the given project.
        """
        self.altern_set = AlternativeSet(self.altern_table_name, self.meta)
        if load_default_altern:
            self.__load_default_alternatives()

    def __load_default_alternatives(self):
        """Load alternatives from the given filename into the DB table.
        """
        for i in range(len(self.default_alternatives)):
            self.altern_set.add_alternative((self.default_alternatives[i]))

    def __create_criteria_set(self, load_default_crit=False):
        """Create a CriteriaSet for the given project.
        """
        self.crit_set = CriteriaSet(self.crit_table_name, self.meta)
        if load_default_crit:
            self.__load_default_criteria()
            
    def __load_default_criteria(self):
        """Load criteria from the given filename into the DB table.
        """
        for row in self.default_criteria:
            self.crit_set.add_criteria((row[0],row[1],row[2], row[3]))

    def __create_mca_runs_table(self):
    	self.mca_runs = McaRuns(self.meta, self.mca_runs_table_name)

    def get_project_data(self):
        return self.project_data.get_project_data()

    def get_project_type(self):
        return self.project_data.get_project_type()

    def add_alternative(self, name):
        """Add alternative to the project AlternativeSet
        
        name (string) - name of alternative
        """
        self.altern_set.add_alternative(name)

    def remove_alternative_by_id(self, alternative_id):
        """Remove alternative from the project AlternativeSet given its unique alternative id
        """
        return self.altern_set.remove_alternative(alternative_id)
    
    def remove_alternative_by_name(self, alternative_name):
        """Remove alternative from the project AlternativeSet given its unique alternative name
        """
        return self.altern_set.remove_alternative_by_name(alternative_name)
        
    def get_alternatives_as_string(self):
        """Get a string representation of the projects AlternativeSet
        """
        if self.altern_set:
            return self.altern_set.to_string()
        else:
            return False

    def get_all_alternatives(self):
        """Returns a list of alternatives in the current project
        """
        return self.altern_set.get_all_alternatives()

    def has_alternatives(self):
        """Returns true if the current project has alternatives loaded
        """
        if self.altern_set.get_num() > 0:
            return True
        else:
            return False
        
    def add_criteria(self, criteria_info):
        """Add criteria to the project CriteriaSet
        
        tuple of criteria data, see CriteriaSet.add_criteria for expected strucutre
        """
        self.crit_set.add_criteria(criteria_info)

    def remove_criteria_by_id(self, criteria_id):
        """Remove criteria from the project CriteriaSet given its unique criteria id
        """
        return self.crit_set.remove_criteria(criteria_id)

    def remove_criteria_by_description(self, description):
        """Remove criteria from the project CriteriaSet given its unique description
        """
        return self.crit_set.remove_criteria_by_description(description)

    def get_criteria_as_string(self):
        """Get a string representation of the projects CriteriaSet
        """
        if self.crit_set:
            return self.crit_set.to_string()
        else:
            return False
    
    def get_all_criteria(self):
        """Returns a list of criteria in the current project
        """
        return self.crit_set.get_all_criteria()

    def get_mca_runs_basic(self):
    	"""Returns a list with basic info about all mca analysis runs for this project
    	"""
    	return self.mca_runs.get_basic()
    
    def get_mca_run_by_id(self, mca_result_id):
    	return self.mca_runs.get_all_by_id(mca_result_id)

    def has_criteria(self):
        """Returns true if the current project has criteria defined
        """
        if self.crit_set.get_num() > 0:
            return True
        else:
            return False
            
    def create_input_matrix(self):
        """Creates an input matrix from the currently defined alternatives and criteria
        
        If the main input table already exists, then creates a new representation in memory, 
        populates it with values from the existing table and then generates a new table
        """
        self.input_matrix = InputMatrix(self.input_matrix_name, self.meta)
     
    def get_input_matrix_as_string(self):
        print "Not Implemented"
        
    def run_mca(self, input_data, input_weights, selected_crit_types):
        evamix = Evamix()
        return evamix.do_analysis(input_data, input_weights, selected_crit_types)

    def save_analysis(self, name, description, altern_data, crit_data, input_data, input_weights, results):        
        self.mca_runs.insert(name, description, altern_data, crit_data, input_data, input_weights, results)

    def delete_analysis(self, id):
        self.mca_runs.delete(id)
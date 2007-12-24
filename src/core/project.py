#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
# @license		GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id$
#===============================================================================

import sqlalchemy
import logging
import os
import sys
import csv
from sqlalchemy import *

from project_data import *
from alternative_set import *
from criteria_set import *
from input_set import *
from mca_runs import *
from delphos_exceptions import *
from csv_types import *

from data import default_alternative_data
from data import default_criteria_data

from evamix.evamix import *

class Project:
    """Represents a delphos project.
    
    Provides functionality to maintain a project including alternatives, criteria and multicriteria 
    analysis results.  In most cases GUI widgets should invoke operations through this object instead of accessing
    lower level core objects directly
    """
    
    def __init__(self, name, path, type=None, load_default_altern=False, load_default_crit=False, language=None):
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
        self.input_table_name = 'input'
        self.input_set = None
        self.mca_runs_table_name = 'mca_runs'
        self.mca_runs = None	#Holds analysis runs for project
        
        #Calculate timezone offset from UTC (greenwich mean time)
        self.utc_offset = time.altzone / 3600
        
        if self.type == "fisheries":
            if language == "english":
                self.default_alternatives = default_alternative_data.fisheries_english_default_alternatives
                self.default_criteria = default_criteria_data.fisheries_english_default_criteria
            if language == "spanish":
                self.default_alternatives = default_alternative_data.fisheries_spanish_default_alternatives
                self.default_criteria = default_criteria_data.fisheries_spanish_default_criteria            
        elif self.type == "mpa":
            if language == "english":
                self.default_alternatives = default_alternative_data.mpa_english_default_alternatives
                self.default_criteria = default_criteria_data.mpa_english_default_criteria
            if language == "spanish":
                self.default_alternatives = default_alternative_data.mpa_spanish_default_alternatives
                self.default_criteria = default_criteria_data.mpa_spanish_default_criteria 
        
        self.__create_project_db()
        if self.status_ok:
            self.__create_project_data()
            self.__create_alternative_set(load_default_altern)
            self.__create_criteria_set(load_default_crit)
            self.__create_input_set()
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

    ################################# Project Data ##############################

    def __create_project_data(self):
        project_name = self.name[:-4]
        self.project_data = ProjectData(self.meta, self.project_table_name, project_name, self.type)

    def get_project_data(self):
        return self.project_data.get_project_data()

    def get_project_type(self):
        return self.project_data.get_project_type()

    ################################# Alternatives ##############################

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

    def num_alternatives(self):
        """Returns number of alternatives for project"""
        if self.altern_set:
            return self.altern_set.get_num()

    def get_alternative_names(self):
        """Returns list of alternative names for project"""
        if self.altern_set:
            return self.altern_set.get_alternative_names()
    
    def get_alternative_id_by_name(self, name):
        """Returns alternative id given an alternative name"""
        if self.altern_set:
            return self.altern_set.get_alternative_id_by_name(name)

    ################################# Criteria ##############################

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
            print row
            self.crit_set.add_criteria((row[0],row[1],row[2], row[3]))

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

    def has_criteria(self):
        """Returns true if the current project has criteria defined
        """
        if self.crit_set.get_num() > 0:
            return True
        else:
            return False

    def num_criteria(self):
        """Returns number of alternatives for project"""
        if self.crit_set:
            return self.crit_set.get_num()

    def get_criteria_id_by_name(self, desc):
        """Returns criteria id given a criteria description"""
        if self.crit_set:
            return self.crit_set.get_criteria_id_by_description(desc)

    ################################# Input ##############################

    def __create_input_set(self):
        """Create a global InputDataSet for the given project.
        """
        self.input_set = InputSet(self.input_table_name, self.meta)

    def get_all_input(self):
        """Returns a list of input for the current project
        """
        if self.input_set:
            return self.input_set.get_all_input()
        else:
            return None

    def get_input_value(self, altern_id, crit_id):
        if self.input_set:
            return self.input_set.get_input_value(altern_id, crit_id)
        else:
            return None

    def update_input_value(self, altern_id, crit_id, value):
        """Updates an input value in the DB"""
        self.input_set.update(altern_id, crit_id, value)

    def remove_input_by_alternative(self, alternative_id):
        return self.input_set.remove_input_by_alternative(alternative_id)

    def remove_input_by_criteria(self, criteria_id):
        return self.input_set.remove_input_by_criteria(criteria_id)

    ################################# Analysis ##############################
    
    def __create_mca_runs_table(self):
    	self.mca_runs = McaRuns(self.meta, self.mca_runs_table_name)

    def get_mca_runs_basic(self):
        """Returns a list with basic info about all mca analysis runs for this project
        """
        return self.mca_runs.get_basic()
    
    def get_mca_run_by_id(self, mca_result_id):
        return self.mca_runs.get_all_by_id(mca_result_id)
 
    def get_num_mca_runs(self):
        return self.mca_runs.get_num()
        
    def run_mca(self, input_data, input_weights, selected_crit_types, selected_crit_bc):
        evamix = Evamix()
        return evamix.do_analysis(input_data, input_weights, selected_crit_types, selected_crit_bc)

    def save_analysis(self, name, description, altern_data, crit_data, input_data, input_weights, results, int_data):        
        self.mca_runs.insert(name, description, altern_data, crit_data, input_data, input_weights, results, int_data)

    def delete_analysis(self, id):
        self.mca_runs.delete(id)
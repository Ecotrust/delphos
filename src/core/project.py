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
from delphos_exceptions import *
from csv_types import *

class Project:
	"""Represents a delphos project.
	
	Provides functionality to maintain a project including alternatives, criteria and multicriteria 
	analysis results.
	"""
	
	def __init__(self, name, path, type=None, load_default_altern=False, load_default_crit=False):
		"""new_project = Project(string, string, string, boolean, boolean)
		
		Default criteria are a predetermined set of criteria thought to be common to
		projects of a given type.  These criteria are stored on disk.
		"""
		self.debug = True
		self.name = name
		self.path = path
		self.type = type
		self.db_driver = 'sqlite'
		self.db_file_ext = '.del'
		self.status_ok = False 	#1-OK, 0-Error
		self.error = ""		#Error message
		
		self.project_table_name = 'project_data'
		self.project_data = None	#General ProjectData
		self.altern_table_name = 'alternatives'
		self.altern_default_file = 'india1_alternatives.csv'
		self.altern_set = None	#Primary AlternativeSet
		
		self.crit_table_name = 'criteria'
		self.crit_default_file = 'india1_criteria.csv'
		self.crit_set = None	#Primary CriteriaSet
		
		self.input_matrix_name = 'input_matrix'
		self.input_default_file = 'india1_data.csv'
		self.input_matrix = None	#Primary input matrix
		
		self.__create_project_db()
		if self.status_ok:
			self.__create_project_data()
			self.__create_alternative_set(load_default_altern)
			self.__create_criteria_set(load_default_crit)
		
	def __create_project_db(self):
		"""Creates a persistent DB for storing project data.
		"""
		#TODO: catch exception
		db = create_engine(self.db_driver+':///'+self.path+os.sep+self.name)
		self.meta = BoundMetaData(db)			#Basically a schema, or table collection
		if self.debug:
			self.meta.engine.echo = True
		self.status_ok = True

	def __create_project_data(self):
		project_name = self.name[:-4]
		self.project_data = ProjectData(self.meta, self.project_table_name, project_name, self.type)

	def __create_alternative_set(self, load_default_altern=False):
		"""Create an AlternativeSet for the given project.
		"""
		self.altern_set = AlternativeSet(self.altern_table_name, self.meta)
		if load_default_altern:
			self.__load_default_alternatives(self.altern_default_file)

	def __load_default_alternatives(self, filename):
		"""Load alternatives from the given filename into the DB table.
		"""
		reader = csv.reader(open("data"+os.sep+filename, "rb"), 'CSV')
		altern_data = []
		for row in reader:
			altern_data.append(row)

		for i in range(len(altern_data)):
			self.altern_set.add_alternative(altern_data[i][0])

	def __create_criteria_set(self, load_default_crit=False):
		"""Create a CriteriaSet for the given project.
		"""
		self.crit_set = CriteriaSet(self.crit_table_name, self.meta)
		
		if load_default_crit:
			self.__load_default_criteria(self.crit_default_file)
			
	def __load_default_criteria(self, filename):
		"""Load criteria from the given filename into the DB table.
		"""
		reader = csv.reader(open("data"+os.sep+filename, "rb"), 'CSV')
		crit_data = []
		for row in reader:
			crit_data.append(row)

		for i in range(len(crit_data)):
			#print crit_data[i]
			self.crit_set.add_criteria(crit_data[i][0],crit_data[i][1],crit_data[i][2])

		self.crit_set.display_table()

	def get_project_data(self):
		return self.project_data.get_project_data()

	def add_alternative(self, name):
		"""Add alternative to the project AlternativeSet
		
		name (string) - name of alternative
		"""
		self.altern_set.add_alternative(name)

	def remove_alternative(self, alternative_id):
		"""Remove alternative from the project AlternativeSet given its unique alternative id
		"""
		return self.altern_set.remove_alternative(alternative_id)
		
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
		print "num criteria: "+str(self.crit_set.get_num())
		if self.altern_set.get_num() > 0:
			return True
		else:
			return False
		
	def add_criteria(self, desc, type, cost_benefit):
		"""Add criteria to the project CriteriaSet
		
		desc (string) - criteria description
		type (int) - see criteria types table
		cost_benefit (string 1) - 'C'=cost or 'B'=benefit
		"""
		self.crit_set.add_criteria(desc, type, cost_benefit)

	def remove_criteria(self, criteria_id):
		"""Remove criteria from the project CriteriaSet given its unique criteria id
		"""
		return self.crit_set.remove_criteria(criteria_id)

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
		print "num criteria: "+str(self.crit_set.get_num())
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
	
	def load_input_from_csv(self, csv_file):
		"""Loads a CSV file into the main input matrix for the current project.
		
		Columns are alternatives, rows are criteria.  The number of columns and rows in the CSV
		should match the number of alternatives and criteria.  An error is displayed if not
		"""
		num_alterns_input = 0
		num_crit_input = 0
		errorMsg = ""
		
		if not csv_file:
			csv_file = self.input_default_file
			
		#Read data from file, row at a time
		reader = csv.reader(open("data"+os.sep+csv_file, "rb"), "CSV")
		input_values = []
		for row in reader:
				input_values.append(row)
		
		#Stuff into 2D array
		for i in range(len(input_values)):
			num_alterns_input = 0
			num_crit_input += 1
			for j in range(len(input_values[i])):
				#Convert cell value from string to integer
				input_values[i][j] = int(input_values[i][j])
				num_alterns_input += 1

		importError = False

		#Verify correct number of columns
		num_alterns_stored = self.altern_set.get_num()
		if num_alterns_input != self.altern_set.get_num():
			errorMsg += '\nIncorrect number of alternatives (columns) in the file. Expected '+str(num_alterns_stored)+', received '+str(num_alterns_input)
			importError = True
		
		#Verify correct number of rows
		num_crit_stored = self.crit_set.get_num()
		if num_crit_input != self.crit_set.get_num():
			errorMsg += '\nIncorrect number of criteria (rows) in the file. Expected '+str(num_crit_stored)+', received '+str(num_crit_input)
			importError = True
		
		if importError:
			raise DataImportError, errorMsg
		
		#Get list of alternative_ids
		altern_ids = self.altern_set.get_alternative_ids()
		#Get list of criteria_ids
		crit_ids = self.crit_set.get_criteria_ids()
				
		#Create InputMatrix
		self.create_input_matrix()

		#Add input data to matrix
		i = 0
		j = 0
		for altern_id in altern_ids:
			for crit_id in crit_ids:
				self.input_matrix.add_input(altern_id, crit_id, input_values[i][j])
				j+=1
			i+=1
		
		self.input_matrix.to_string()
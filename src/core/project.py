import sqlalchemy
import logging
import os
import sys
import csv
from sqlalchemy import *
from alternative_set import *
from criteria_set import *
from input_matrix import *

csv.register_dialect("csv",csv.excel)

class Project():
	"""Represents a delphos project.
	
	Provides functionality to maintain a project including alternatives, criteria and multicriteria 
	analysis results.
	"""
	
	def __init__(self, name, path, load_default_crit=False):
		"""new_project = Project(string, string, boolean)
		
		Default criteria are a predetermined set of criteria thought to be common to
		projects of a given type.  These criteria are stored on disk.
		"""
		self.debug = True
		self.name = name
		self.path = path
		self.db_driver = 'sqlite'
		self.db_file_ext = 'del'
		self.status_ok = False 	#1-OK, 0-Error
		self.error = ""		#Error message
		
		self.altern_table_name = 'alternatives'
		self.altern_set = None	#Primary AlternativeSet
		
		self.crit_table_name = 'criteria'
		self.crit_base_file = 'base_criteria.csv'
		self.crit_set = None	#Primary CriteriaSet
		
		self.input_matrix_name = 'input_matrix'
		self.input_matrix = None	#Primary input matrix
		
		self.__create_project_db()
		if self.status_ok:
			self.__create_alternative_set()
			self.__create_criteria_set(load_default_crit)
		
	def __create_project_db(self):
		"""Creates a persistent DB for storing project data.
		"""
		#TODO: catch exception
		db = create_engine(self.db_driver+':///'+self.path+os.sep+self.name+'.'+self.db_file_ext)
		self.meta = BoundMetaData(db)			#Basically a schema, or table collection
		if self.debug:
			self.meta.engine.echo = True
		self.status_ok = True

	def __create_alternative_set(self):
		"""Create an AlternativeSet for the given project.
		"""
		self.altern_set = AlternativeSet(self.altern_table_name, self.meta)

	def __create_criteria_set(self, load_default_crit=False):
		"""Create a CriteriaSet for the given project.
		"""
		self.crit_set = CriteriaSet(self.crit_table_name, self.meta)
		
		if load_default_crit:
			self.__load_default_criteria(self.crit_base_file)
			
	def __load_default_criteria(self, filename):
		"""Load criteria from the given filename into the DB table.
		"""
		reader = csv.reader(open("data"+os.sep+filename, "rb"), 'csv')
		crit_data = []
		for row in reader:
			crit_data.append(row)

		for i in range(len(crit_data)):
			#print crit_data[i]
			self.crit_set.add_criteria(crit_data[i][0],crit_data[i][1],crit_data[i][2])

		self.crit_set.display_table()

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

	def has_alternatives(self):
		"""Returns true if the current project has alternatives loaded
		"""
		print "num criteria: "+str(self.crit_set.get_num_criteria())
		if self.altern_set.get_num_alternatives() > 0:
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
			
	def has_criteria(self):
		"""Returns true if the current project has criteria defined
		"""
		print "num criteria: "+str(self.crit_set.get_num_criteria)
		if self.crit_set.get_num_criteria() > 0:
			return True
		else:
			return False
			
	def create_input_matrix():
		"""Creates an input matrix from the currently defined alternatives and criteria
		
		If the main input table already exists, then creates a new representation in memory, 
		populates it with values from the existing table and then generates a new table
		"""
		print "Not Implemented"
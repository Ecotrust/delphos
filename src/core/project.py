import sqlalchemy
import logging
import os
import sys
import csv
from sqlalchemy import *
from criteria_set import *

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
		self.crit_base_file = 'base_criteria.csv'
		self.crit_table_name = 'criteria'
		self.db_driver = 'sqlite'
		self.db_file_ext = 'del'
		self.status_ok = False 	#1-OK, 0-Error
		self.error = ""		#Error message
		
		print "creating project"
		
		self.__create_project_db()
		if self.status_ok:
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
		
	def __create_criteria_set(self, load_default_crit=False):
		"""Create a CriteriaSet for the given project.
		"""
		self.crit_set = None
		self.crit_set = CriteriaSet(self.crit_table_name, self.meta)

		print "load defaults?: "+str(load_default_crit)
		
		if load_default_crit:
			print "loading defaults"
			self.__load_default_criteria(self.crit_base_file)

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
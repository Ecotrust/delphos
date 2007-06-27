import sqlalchemy
import logging
import os
import sys
import csv
from sqlalchemy import *
from criteria_set import *

csv.register_dialect("csv",csv.excel)

class Project():
	def __init__(self, name, path):
		self.debug = True
		self.name = name
		self.path = path
		self.crit_base_file = 'base_criteria.csv'
		self.crit_table_name = 'criteria'
		self.db_driver = 'sqlite'
		self.db_file_ext = 'db'
		self.status = 0 	#0-OK, 1-Error
		self.error = ""		#Error message
		
		self.create_project_db()
		
	def create_project_db(self):
		#TODO: catch exception
		db = create_engine(self.db_driver+':///'+self.path+os.sep+self.name+'.'+self.db_file_ext)
		self.meta = BoundMetaData(db)			#Basically a schema, or table collection
		if self.debug:
			self.meta.engine.echo = True
		
	def create_criteria_set(self, load_defaults=False):		
		self.crit_set = None
		self.crit_set = CriteriaSet(self.crit_table_name, self.meta)

		print self.crit_set.get_num_criteria()

		if load_defaults:
			self.__load_default_criteria(self.crit_base_file)

	def get_criteria_as_string(self):
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
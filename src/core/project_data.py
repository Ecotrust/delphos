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

from sqlalchemy import *
import os
import sys

from util.common_functions import *

class ProjectData(object):
	"""Provides access to a projects info
	"""
	def __init__(self, metadata, db_name, project_name, type):
		"""project_data = ProjectData(BoundMetadata, string, string, string)
		
		metadata - SQLAlchemy metadata object providing access to DB engine and tables
		db_name - name to give DB
		project_name - name of project
		type - analaysis type (eg. fisheries or mpa)
		"""
 		self.metadata = metadata
		self.db_name = db_name
		self.project_name = project_name
		self.project_type = type
		self.project_created = ""
		
		self.table = None
		self.mapper = None
		
		#Load project table from DB if it exists otherwise create it
		if self.metadata.engine.has_table(self.db_name):
			self.table = Table(self.db_name, self.metadata, autoload=True)
			self.load_project_data()
		else:
			self.__create_project_data_table()
			self.insert_project_data()
		
		#print list(self.table.columns)

	def __create_project_data_table(self):
		"""Create a new project data table in the DB
		"""
		self.table = self.__get_project_data_table_object()
		self.table.create()
	
	def __get_project_data_table_object(self):
		"""Create project data Table object (SQLAlchemy)
		"""
		return Table(self.db_name, self.metadata,
			Column('name', String(200), primary_key=True),
			Column('type', String(200)),
			Column('created', DateTime(timezone=True))
		)

	def load_project_data(self):
		"""Load project data from the DB into this ProjectData instance
		"""
		i = self.table.select().execute()
		data = i.fetchone()
		(self.project_name, self.project_type, self.project_created) = data

	def insert_project_data(self):
		self.table.insert().execute({'name':self.project_name, 'type':self.project_type, 'created':func.current_timestamp()})

	def get_project_data(self):
		if not self.project_created:
			self.load_project_data()
			
		return (self.project_name, self.project_type, utc_to_local_time(self.project_created))

	def get_project_type(self):
		if self.project_type:
			return self.project_type
		else:
			return None

	def __unicode__(self):
		"""Description of object
		"""
		return "ProjectData"
	
	def __str__(self):
		"""Description of object
		"""
		return "ProjectData"
	
	def to_string(self):
		"""Returns string representation of the ProjectData
		"""
		i = self.table.select().execute()
		proj_data_str = i.fetchone()
		return str(proj_data_str)
	
#Testing purposes
if __name__ == '__main__':
 	os.chdir('..')	#Go to top-level directory
	db = create_engine('sqlite:///db/project23.del')
	meta = BoundMetaData(db)	#Basically a schema, or table collection
	proj_data = ProjectData('project_data', meta)
	#print proj_data.to_string()
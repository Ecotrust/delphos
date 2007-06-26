import os
import sqlalchemy
import logging
from sqlalchemy import *

from project import *

class ProjectManager:
	def __init__(self):
		self.current_project_name = ""
		self.current_project_path = ""
		self.current_project = None
		self.default_project_path = "db"
		self.db_driver = 'sqlite'

	def create_project(self, name, path):

		if not path:
			path = self.default_project_path

		#Check if DB already exists
		db_path = path+os.sep+name+".db"
		if os.path.exists(db_path):
			print "\nProject named "+name+" already exists at "+path
			return False

		#Create DB URL
		db_url = self.db_driver+':///'+path
		
		#Create project
		proj = Project(name, path)
		if not proj:
			print "\nProject creation failed"
			return False

	def get_current_project(self):
		return self.current_project
		
	def set_current_project(self, name):
		self.current_project = name

	def get_current_project_name(self):
		return self.current_project_name

	def validate_project_name(self, name):
		if name:
			return True

	def get_default_project_path(self):
		return self.default_project_path

	def validate_project_path(self, path):
		if os.path.exists(path):
			return True
		else:
			return False
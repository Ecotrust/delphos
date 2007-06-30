import os
import logging
from sqlalchemy import *
from project import *

class ProjectManager:
	"""Provides access to, handles and maintins delphos projects.
	"""
	def __init__(self):
		self.current_project_name = ""
		self.current_project_path = ""
		self.current_project = None
		self.default_project_path = "db"

	def create_project(self, name, path, load_default_altern, load_default_crit):
		"""Create a new delphos Project
	
		name (string) - name of the project
		path (string) - path, relative or absolute, to store project DB
		"""
		
		#If project already open then close it first
		if self.current_project:
			self.close_current_project()
		
		if not path:
			path = self.default_project_path

		#Check if DB already exists
		db_path = path+os.sep+name+".del"
		if os.path.exists(db_path):
			print "\nProject named "+name+" already exists at "+path
			return False
		
		#Create project
		proj = Project(name, path, load_default_altern, load_default_crit)
		if not proj:
			print "\nProject creation failed"
			return False
		
		self.current_project = proj
		self.current_project_name = name
		return True

	def open_project(self, name, path):
		"""Open an existing delphos Project
	
		name (string) - name of the project
		path (string) - path, relative or absolute, that DB is stored
		"""		
		if self.current_project:
			self.close_current_project()
		
		if not path:
			path = self.default_project_path

		#Verify DB already exists
		db_path = path+os.sep+name+".del"
		if not os.path.exists(db_path):
			print "\nProject named "+name+" doesn't exist at "+path
			return False
		
		#Create Project
		proj = Project(name, path)
		if not proj:
			print "\nProject open failed"
			return False
		
		self.current_project = proj
		self.current_project_name = name
		return True

	def close_current_project(self):
		self.current_project = None
		self.current_project_name = ""
		self.current_project_path = ""
		clear_mappers()

	def get_current_project(self):
		"""Returns reference to current Project object
		"""
		if self.current_project:
			return self.current_project
		else:
			return False

	def get_current_project_name(self):
		"""Returns name of current project
		"""
		return self.current_project_name

	def validate_project_name(self, name):
		"""Verifies that a given name is suitable for use a a project name
		"""
		if name:
			return True

	def get_default_project_path(self):
		"""Returns the default path that projects are stored if one is not given
		"""
		return self.default_project_path

	def validate_project_path(self, path):
		"""Verifies that a given project path is valid
		"""
		if os.path.exists(path):
			return True
		else:
			return False
		
#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory
	project_manager = ProjectManager()

#	load_default_criteria = True
#	cur_proj = project_manager.create_project('project2','db', load_default_criteria)

	cur_proj = project_manager.open_project('project2','db')
	cur_proj.add_criteria('Crikey',2,'C')
	cur_proj.remove_criteria(27)
	crit_str = cur_proj.get_criteria_as_string()
	print crit_str
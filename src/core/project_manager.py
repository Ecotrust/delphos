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

	def create_project(self, name, path):
		if not path:
			path = self.default_project_path

		#Check if DB already exists
		db_path = path+os.sep+name+".db"
		if os.path.exists(db_path):
			print "\nProject named "+name+" already exists at "+path
			return False
		
		#Create project
		proj = Project(name, path)
		if not proj:
			print "\nProject creation failed"
			return False
		
		self.current_project = proj
		return proj

	def open_project(self, name, path):
		if not path:
			path = self.default_project_path

		#Verify DB already exists
		db_path = path+os.sep+name+".db"
		if not os.path.exists(db_path):
			print "\nProject named "+name+" doesn't exist at "+path
			return False
		
		#Create Project
		proj = Project(name, path)
		if not proj:
			print "\nProject open failed"
			return False
		
		self.current_project = proj
		return proj

	def get_current_project(self):
		if self.current_project:
			return self.current_project
		else:
			return False

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
		
#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory
	project_manager = ProjectManager()
	#cur_proj = project_manager.create_project('project2','db')
	cur_proj = project_manager.open_project('project2','db')
	crit_str = cur_proj.get_criteria_as_string()

	#if cur_proj:
	#	load_defaults = True
	#	cur_proj.create_criteria_set(load_defaults)
	#else:
	#	print "No project to load"
	
	#delphos_manager.g_crit_set.add_criteria('Crikey',2,'C')
	#delphos_manager.g_crit_set.remove_criteria(27)
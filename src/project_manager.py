import os
from project import *

class ProjectManager:
	def __init__(self):
		self.projects = []
		self.current_project_name = "";
		self.current_project = None;
		self.current_project_path = "";
		self.default_project_path = os.getcwd()+os.sep+'db'

	def create_project(self, name, path):
		#If no path provided use default
		if not path:
			path = self.default_project_path
			
		#Check if project DB already exists
		db_name = path+os.sep+name+".db"
		if os.path.exists(db_name):
			print "\nProject named "+name+" already exists at "+path
			return False
		
		#Create project
		proj = Project(name)
		if proj:
			self.current_project = proj
			self.current_project_name = name
			return True
		else:
			print "\nProject creation failed"
			return False

	def get_current_project(self):
		return self.current_project;
		
	def set_current_project(self, name):
		self.current_project = name;

	def get_current_project_name(self):
		return self.current_project_name;

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
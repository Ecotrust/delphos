import os
import sys
import logging
from project_manager import *
from sqlalchemy import *


if __name__ == '__main__':
	proj_manager = ProjectManager()
	
	default_proj_path = os.getcwd()+os.sep+'db'
	proj_path = ""
	
	while True:
#		if not proj_path:
#			proj_path = raw_input('\nProject Working Path? ['+default_proj_dir+']')
#			
#			if proj_dir:
#				if not os.path.exists(proj_dir):
#					continue
#			else:
#				proj_dir = default_proj_dir
#		
#			print "current project directory: "+proj_dir

		print """
Delphos Menu

(C)reate project
(O)pen project"""

		menu_opt = raw_input('\nEnter Option:')
		
		if menu_opt == 'c':
			#Get project name (TODO: constrain possible characters)
			proj_name = raw_input('\nChoose a project name:')
			
			#Get a legal project path
			path_exists = false
			while not path_exists:
				proj_path = raw_input('\nChoose a project directory ['+default_proj_dir+']:')
			
				if not proj_path:
					proj_path = default_proj_path
				
				if not os.path.exists(proj_path):
					path_exists = false
					
			proj_manager.createProject(proj_name, proj_path)
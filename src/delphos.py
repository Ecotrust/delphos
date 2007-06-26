import os
import sys
import logging
from core.project_manager import *
from core.project import *
from sqlalchemy import *

if __name__ == '__main__':

	def main_menu():
		print "\nDelphos Menu\n\n(C)reate project\n(O)pen project\n(Q)uit"
		menu_opt = raw_input('\nEnter Option:')
		
		if menu_opt == 'c' or menu_opt == 'C':
			proj_name = None
			while not project_manager.validate_project_name(proj_name):
				proj_name = raw_input('\nChoose a project name:')
				
			proj_path = None
			proj_path = raw_input('\nChoose a project directory ['+project_manager.get_default_project_path()+']:')	
			if proj_path: #if non-empty validate it
				while not proj_path or not project_manager.validate_project_path(proj_path):
					proj_path = raw_input('\nChoose a project directory ['+project_manager.get_default_project_path()+']:')
	
			project_manager.create_project(proj_name, proj_path)

		elif menu_opt == 'o' or menu_opt == 'O':
			proj_path = None
			proj_path = raw_input('\nChoose a project directory ['+project_manager.get_default_project_path()+']:')

		elif menu_opt == 'q' or menu_opt == 'Q':
			sys.exit()
			
	def project_menu():
		print "\nProject Menu\ncurrent project: "+project_manager.get_current_project_name()+"\n\n(Q)uit"
		menu_opt = raw_input('\nEnter Option:')
		
		if menu_opt == 'q' or menu_opt == 'Q':
			sys.exit()

	project_manager = ProjectManager()
	while True:
		if not project_manager.get_current_project_name():
			main_menu()
		else:
			project_menu()
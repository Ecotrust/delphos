import os
import sys
import logging
from core.project_manager import *
from core.project import *
from sqlalchemy import *

if __name__ == '__main__':

	def main_menu(cur_menu):
		#cls()
		print "\nDelphos Menu\n\n(C)reate new project\n(O)pen project"
		if project_manager.get_current_project():
			print "(B)ack to project menu"
		print "(Q)uit"
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
			
			default_crit_answer = raw_input('\nLoad default criteria? [Y]:')
			load_default_crit = True
			if default_crit_answer == 'N' or default_crit_answer == 'n':
				load_default_crit = False
	
			isLoaded = project_manager.create_project(proj_name, proj_path, load_default_crit)
			if isLoaded:
				cur_menu[0] = 'project'

		elif menu_opt == 'o' or menu_opt == 'O':
			proj_path = None
			proj_name = None
			
			proj_path = raw_input('\nChoose a project directory ['+project_manager.get_default_project_path()+']:')
			proj_name = raw_input('\nProject Name: ')

			isLoaded = project_manager.open_project(proj_name, proj_path)
			if isLoaded:
				cur_menu[0] = 'project'

		elif menu_opt == 'b' or menu_opt == 'B':
			cur_menu[0] = 'project'
			
		elif menu_opt == 'q' or menu_opt == 'Q':
			sys.exit()
			
	def project_menu(cur_menu):
		#cls()
		print "\nProject Menu\ncurrent project: "+project_manager.get_current_project_name()+"\n\n(L)ist criteria\n(A)dd criteria\n(R)emove criteria\n(B)ack to main menu\n(Q)uit"
		menu_opt = raw_input('\nEnter Option:')
		
		if menu_opt == 'q' or menu_opt == 'Q':
			sys.exit()

		elif menu_opt == 'l' or menu_opt == 'L':
			cur_proj = project_manager.get_current_project()
			if cur_proj:
				crit_str = cur_proj.get_criteria_as_string()		
				cls()
				print crit_str
			else :
				print "Project not loaded!"
		
		elif menu_opt == 'a' or menu_opt == 'A':
			desc = raw_input('\nCriteria description: ')
			type = raw_input('Criteria type [1:bliff, 2:blam, 3:blort]: ')
			cb = raw_input('(C)ost or (B)enefit [C]: ')
			crit_str = project_manager.get_current_project().add_criteria(desc, type, cb)
		
		elif menu_opt == 'r' or menu_opt == 'R':
			id = raw_input('\nCriteria ID:')
			success = project_manager.get_current_project().remove_criteria(id)
		
		elif menu_opt == 'b' or menu_opt == 'B':
			cur_menu[0] = 'main'

	def cls():
		"""Clear screen.
		"""
		for i in range(40):
			print ""

	project_manager = ProjectManager()

	cur_menu = ['main']
	while True:
		#if not project_manager.get_current_project():
		if cur_menu[0] == 'main':
			main_menu(cur_menu)
		elif cur_menu[0] == 'project':
			project_menu(cur_menu)
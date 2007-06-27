from sqlalchemy import *
import logging
import os
import sys

class DelphosManager(object):
	def __init__(self):
		self.debug = True

	def copy_criteria_subset(self):
		print "stubby"
	
	def create_criteria_options(self):
		print "stubby"

#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory
	delphos_manager = DelphosManager()
	#delphos_manager.g_crit_set.add_criteria('Crikey',2,'C')
	#delphos_manager.g_crit_set.remove_criteria(27)
from sqlalchemy import *
import logging
import csv
import os
from criteria_set import CriteriaSet

csv.register_dialect("csv",csv.excel)

class CriteriaManager(object):
	def __init__(self):
		self.g_table_name = 'global_criteria'
		self.g_db_name = self.g_table_name+'.db'
		self.db_driver = 'sqlite'
		self.debug = True
		self.global_base_criteria_file = 'base_criteria.csv'
		
		#SQLAlchemy specific
		self.db = create_engine(self.db_driver+':///db/'+self.g_db_name)
		self.metadata = BoundMetaData(self.db)	#Basically a schema, or a table collection
		self.g_criteria_set = None
		
		if self.debug:
			self.metadata.engine.echo = True
		
		#Create global criteria set
		self.g_criteria_set = CriteriaSet(self.g_table_name, self.metadata)
		
		#Load global criteria set if it isn't already
		if self.g_criteria_set.get_num_criteria() == 0:
			self.load_global_criteria_from_file(self.global_base_criteria_file)

	#Load criteria from the given filename into the DB table
	def load_global_criteria_from_file(self, filename):
		reader = csv.reader(open("data"+os.sep+filename, "rb"), 'csv')
		crit_data = []
		for row in reader:
			crit_data.append(row)

		for i in range(len(crit_data)):
			#print crit_data[i]
			self.g_criteria_set.add_criteria(crit_data[i][0],crit_data[i][1],crit_data[i][2])

		self.g_criteria_set.display_table()

	def copy_criteria_subset(self):
		print "stubby"
	
	def create_criteria_options(self):
		print "stubby"

#Testing purposes
if __name__ == '__main__':
	criteria_manager = CriteriaManager()
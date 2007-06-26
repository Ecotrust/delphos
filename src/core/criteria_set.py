from sqlalchemy import *
import logging

#Represents a set of criteria which can be added and removed.  Abstracts the details of working with
#the underlying database table
class CriteriaSet(object):
	def __init__(self, name, metadata):
		self.name = name
		self.metadata = metadata
		self.table = None
		
		if self.metadata.engine.has_table(self.name):
			#Load existing table
			self.table = Table(self.name, self.metadata, autoload=True)
		else:
			#Create table
			self.__create_criteria_table__()
		print list(self.table.columns)

	def __create_criteria_table__(self):
		self.table = Table(self.name, self.metadata,
			Column('criteria_id', Integer, Sequence('crit_id_seq'), primary_key=True),
			Column('description', String(200)),
			Column('type', Integer),
			Column('cost_benefit', String(1))
		)
		self.table.create()
		
	def add_criteria(self, desc, type, cost_benefit):
		self.table.insert().execute({'description':desc, 'type':type, 'cost_benefit':cost_benefit})
	
	def remove_criteria(self):
		print "stubby"
	
	def get_num_criteria(self):
		thecol = self.table.c.criteria_id
		result = self.table.select(thecol).execute()
		row = result.fetchone()
		print result.rowcount
		if row is None:
			return 0
			
#		print row.keys()
#		num_cols = row[self.table.c.criteria_id]
#		return num_cols

	def display_table(self):
		i = self.table.select().execute()
		ir = i.fetchall()
		for input in ir:
			print input

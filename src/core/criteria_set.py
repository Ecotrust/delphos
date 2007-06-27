from sqlalchemy import *
import logging
import sys

#Represents a set of criteria which can be added and removed from.  Abstracts the details of working with
#the underlying Criteria table and mapper
class CriteriaSet(object):
	def __init__(self, name, metadata):
		self.name = name
		self.metadata = metadata
		self.table = None
		self.mapper = None
		
		#Load criteria table from DB if it exists otherwise create it
		if self.metadata.engine.has_table(self.name):
			self.table = Table(self.name, self.metadata, autoload=True)
		else:
			self.__create_criteria_table()
		
		#Map Criteria object to criteria table
		self.mapper = mapper(Criteria, self.table)
		
		#print list(self.table.columns)

	def __create_criteria_table(self):
		self.table = self.get_criteria_table_object()
		self.table.create()
	
	def get_criteria_table_object(self):
		return Table(self.name, self.metadata,
			Column('criteria_id', Integer, Sequence('crit_id_seq'), primary_key=True),
			Column('description', String(200)),
			Column('type', Integer),
			Column('cost_benefit', String(1))
		)
		
	def add_criteria(self, desc, type, cost_benefit):
		self.table.insert().execute({'description':desc, 'type':type, 'cost_benefit':cost_benefit})
	
	def remove_criteria(self, criteria_id):
		self.table.delete(self.table.c.criteria_id==criteria_id).execute()
	
	def get_num_criteria(self):
		session = create_session(bind_to=self.metadata.engine)
		return session.query(self.mapper).count()

	def __unicode__(self):
		return "hola"
	
	def __str__(self):
		return "yo"
	
	def to_string(self):
		i = self.table.select().execute()
		ir = i.fetchall()
		print ir
		sys.exit()
#		for input in ir:
#			print input		

	def display_table(self):
		i = self.table.select().execute()
		ir = i.fetchall()
		for input in ir:
			print input

class Criteria(object):
	"""For mapping onto criteria tables using SQLAlchemy and accessing in an object-oriented way
	"""
	pass
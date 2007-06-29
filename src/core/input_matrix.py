from sqlalchemy import *
import os
import sys

class InputMatrix(object):
 	"""Represents a matrix of values formed from the pairing of each alternative with each criteria
	"""
	def __init__(self, name, metadata):
		"""input_matrix = InputMatrix(string, BoundMetadata)
		
		name - name of the input matrix and ultimately the underlying DB table
		metadata - SQLAlchemy metadata object providing access to DB engine and tables
		"""
		self.name = name
		self.metadata = metadata
		self.table = None
		self.mapper = None
		
		#Load input values from DB if they exist otherwise create a new input table
		if self.metadata.engine.has_table(self.name):
			self.table = Table(self.name, self.metadata, autoload=True)
		else:
			self.__create_input_table()
		
		#Map InputMatrix object to Input table
		self.mapper = mapper(Input, self.table)
		
		#print list(self.table.columns)

	def __create_input_table(self):
		"""Create a new input table in the DB
		"""
		self.table = self.__get_input_table_object()
		self.table.create()
	
	def __get_input_table_object(self):
		"""Create input Table object (SQLAlchemy)
		"""
		return Table(self.name, self.metadata,
			Column('alternative_id', Integer, primary_key=True),
			Column('criteria_id', Integer, primary_key=True),
			Column('value', Integer)
		)
		
	def add_input(self, alternative_id, criteria_id, value):
		"""Add input to the InputMatrix
		
		alternative_id (int) - unique id of the alternative
		criteria_id (int) - unique id of the criteria
		value (int) - value to associate with alt/crit pair
		"""
		self.table.insert().execute({'name':name})
	
	def remove_alternative(self, alternative_id):
		"""Remove value from InputMatrix given its associated alternative_id and criteria_id
		"""
		result = self.table.delete(self.table.c.alternative_id==alternative_id).execute()
		#TODO : verify this is True
		return True

	def __unicode__(self):
		"""Description of object
		"""
		return "InputMatrix"
	
	def __str__(self):
		"""Description of object
		"""
		return "InputMatrix"
	
	def to_string(self):
		"""Returns string representation of the InputMatrix
		"""
		return "Not Implemented"

class Input(object):
	"""Input class maps to Input DB tables allowing access to them in OO way using SQLAlchemy
	
	Members for this class are created dynamically by SQLAlchemy at the time of mapping.  Member
	names correspond directly to names of attributes in the table mapped to.
	"""
	pass
	
#Testing purposes
if __name__ == '__main__':
 	os.chdir('..')	#Go to top-level directory
	db = create_engine('sqlite:///db/project23.del')
	meta = BoundMetaData(db)	#Basically a schema, or table collection
from sqlalchemy import *
import logging
import sys

class CriteriaSet(object):
	"""Represents a set of analysis criteria.
	"""
	def __init__(self, name, metadata):
		"""crit_set = CriteriaSet(string, BoundMetadata)
		
		name - name of criteria set and ultimately the underlying DB table
		metadata - SQLAlchemy metadata object providing access to DB engine and tables
		"""
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
		"""Create a new criteria table in the DB
		"""
		self.table = self.__get_criteria_table_object()
		self.table.create()
	
	def __get_criteria_table_object(self):
		"""Create criteria Table object (SQLAlchemy)
		"""
		return Table(self.name, self.metadata,
			Column('criteria_id', Integer, Sequence('crit_id_seq'), primary_key=True),
			Column('description', String(200)),
			Column('type', Integer),
			Column('cost_benefit', String(1))
		)
		
	def add_criteria(self, desc, type, cost_benefit):
		"""Add criteria to the CriteriaSet
		
		desc (string) - criteria description
		type (int) - see criteria types table
		cost_benefit (string 1) - 'C'=cost or 'B'=benefit
		"""
		self.table.insert().execute({'description':desc, 'type':type, 'cost_benefit':cost_benefit})
	
	def remove_criteria(self, criteria_id):
		"""Remove criteria from CriteriaSet given its unique criteria id
		"""
		result = self.table.delete(self.table.c.criteria_id==criteria_id).execute()
		#TODO : verify this is True
		return True
		
	
	def get_num_criteria(self):
		"""Returns the number of criteria stored in the CriteriaSet
		"""
		session = create_session(bind_to=self.metadata.engine)
		return session.query(self.mapper).count()

	def __unicode__(self):
		"""Description of object
		"""
		return "CriteriaSet"
	
	def __str__(self):
		"""Description of object
		"""
		return "CriteriaSet"
	
	def to_string(self):
		"""Returns string representation of the CriteriaSet
		"""
		i = self.table.select().execute()
		ir = i.fetchall()
		crit_str = ""
		for row in ir:
			crit_str += str(row)+"\n"
		if crit_str == "":
			crit_str = "No criteria defined"
		return crit_str

	def display_table(self):
		"""Prints a string representation of the CriteriaSet
		"""
		i = self.table.select().execute()
		ir = i.fetchall()
		for input in ir:
			print input

class Criteria(object):
	"""Criteria class maps to criteria DB tables allowing access to them in OO way using SQLAlchemy
	
	Members for this class are created dynamically by SQLAlchemy at the time of mapping.  Member
	names correspond directly to names of attributes in the table mapped to.
	"""
	pass
#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
# @license		GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id$
#===============================================================================

from sqlalchemy import *
import pickle
import sys

from delphos_exceptions import *

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
		
		the type_options column is Binary so that it can store pickled strings and not make assumptions about
		encoding etc. 
		"""
		return Table(self.name, self.metadata,
			Column('criteria_id', Integer, Sequence('crit_id_seq'), primary_key=True),
			Column('description', Unicode(200)),
			Column('type', Unicode(50)),
			Column('type_options', Binary()),
			Column('cost_benefit', Unicode(1))
		)
		
	def add_criteria(self, criteria_info):
		"""Add criteria to the CriteriaSet
		
		Expected input tuple structure:
		desc (unicode) - criteria description
		type (unicode) - Ratio, Binary or Ordinal
		type_options (string or list depending on type):
			Ratio (string description), Binary ([yes_desc, no_desc]), 
			Ordinal (list of option lists [[description, value],...])
			* Note type_data is simply pickled (serialized) and put into 
			* the DB table as given. SQLA can only pickle strings and lists, not tuples
		cost_benefit (string) - 'C'=cost or 'B'=benefit
		"""
		#print "info to add: "+unicode(criteria_info)
		(desc, type, type_options, cost_benefit) = criteria_info
		#Pickle the type_options up
		type_options = pickle.dumps(type_options)
		same_list = list(self.table.select(self.table.c.description==desc).execute())
		#print "same_list: "+unicode(same_list)
		if len(same_list) > 0:
			raise DelphosError, "A criterion with the description '"+desc+"' already exists in this project."
		else:
			#print "inserting"
			self.table.insert().execute({'description':desc, 'type':type, 'type_options':type_options, 'cost_benefit':cost_benefit})
	
	def remove_criteria(self, criteria_id):
		"""Remove criteria from CriteriaSet given its unique criteria id
		"""
		result = self.table.delete(self.table.c.criteria_id==criteria_id).execute()
		#TODO : verify this is True
		return True

	def remove_criteria_by_description(self, description):
		"""Remove criteria from CriteriaSet given its unique description
		"""
		result = self.table.delete(self.table.c.description==description).execute()
		#TODO : verify this is True
		return True
		
	def get_all_criteria(self):
		"""Returns criteria as a list
		"""
		#return list(self.table.select(order_by=self.table.c.criteria_id).execute())
		criteria_rows = self.table.select(order_by=self.table.c.criteria_id).execute().fetchall()
		criteria_recs = []
		for row in criteria_rows:
			cur_row = list(row)
			#unpickle the options
			#TODO: find out why SQLA is not unpickleing for us!
			cur_row[3] = pickle.loads(cur_row[3])
			#for i in range(len(cur_row[3])):
			#	cur_row[3][i][0] = unicode(cur_row[3][i][0])
			criteria_recs.append(cur_row)
		return criteria_recs
		
	def get_criteria_ids(self):
		"""Returns list of IDs of criteria currently loaded
		"""
		crit_id_list = []
		for row in self.table.select(order_by=self.table.c.criteria_id).execute():
			crit_id_list.append(row.criteria_id)
		return crit_id_list	

	def get_criteria_id_by_description(self, desc):
		"""Returns criteria id given a criteria description"""
		result = self.table.select(self.table.c.description==desc).execute()
		if result:
			row = result.fetchone()
			if row:
				return row.criteria_id
			else:
				return None
		else:
			return None

	def get_num(self):
		"""Returns the number of criteria stored in the CriteriaSet
		"""
		session = create_session(bind_to=self.metadata.engine)
		return int(session.query(self.mapper).count())

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

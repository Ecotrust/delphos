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
#
# @summary - Used to store, edit and retreieve global input data for a project
# from a db. 
#===============================================================================

from sqlalchemy import *
from delphos_exceptions import *
import os
import sys

class InputSet():
	"""Maintains global input by the user for a project.
	
	Rows in a table represent a value for a given alternative/crit id pair
	
	Ties input values to their associated altern/criteria pair so
	that the user can go back and change the altern and crit without losing
	the data that they already input.  It also separates data from 
	presentation.
	
	input_data: [[[altern_data][crit_data][row][col][value]], ...]
	altern_data: (altern_id, altern_name, altern_color)
	crit_data: (crit_id, crit_name, crit_type, crit_options_units, cost_benefit)
	"""
	
	def __init__(self, name, metadata):
		"""altern_set = InputSet(string, BoundMetadata)
		
		name - name of input set and ultimately the underlying DB table
		metadata - SQLAlchemy metadata object providing access to DB engine and tables
		"""
		self.name = name
		self.metadata = metadata
		self.table = None
		self.mapper = None
		
		#Load input table from DB if it exists otherwise create it
		if self.metadata.engine.has_table(self.name):
			self.table = Table(self.name, self.metadata, autoload=True)
		else:
			self.__create_input_table()
		
		#Map input object to input table
		self.mapper = mapper(Input, self.table)
		
	def __create_input_table(self):
		"""Create a new input table in the DB
		"""
		self.table = self.__get_input_table_object()
		self.table.create()
	
	def __get_input_table_object(self):
		"""Create input Table object (SQLAlchemy)
		"""
		return Table(self.name, self.metadata,
			Column('altern_id', Integer, primary_key=True),
			Column('crit_id', Integer, primary_key=True),
			Column('value', Integer)
		)
		
	def add_input(self, altern_id, crit_id, value):
		"""Add input to the InputSet
		
		altern_name (string) - name of the input
		"""
		#Verify altern exists with given id
		#Verify crit exists with given id (and value matches crit option if binary or ordinal)  
		altern_exists = True
		crit_exists = True
		valid_value = True
		if altern_exists and crit_exists and valid_value:
			self.table.insert().execute({'altern_id':altern_id, 'crit_id':crit_id, 'value': value})
		else:
			raise DelphosError, "Error"
	
	def update(self, altern_id, crit_id, value):
		self.remove_input_by_ids(altern_id, crit_id)
		if value is not None:
			self.add_input(altern_id, crit_id, value)

	def get_input_value(self, altern_id, crit_id):
		"""Return input value given an altern and crit id
		"""
		sql = self.table.select( and_(self.table.c.altern_id==altern_id, self.table.c.crit_id==crit_id) )
		result = sql.execute()
		if result:
			row = result.fetchone()
			if row:
				return row.value
			else:
				return None
		else:
			return None
	
	def remove_input_by_ids(self, altern_id, crit_id):
		"""Remove input from InputSet given its unique input id
		"""
		sql = self.table.delete( and_(self.table.c.altern_id==altern_id, self.table.c.crit_id==crit_id) )
		result = sql.execute()
		#TODO : verify removal
		return True

	def get_all_input(self):
		"""Returns all inputs in set in list structure [[id, name], ...]
		"""
		return list(self.table.select(order_by=self.table.c.altern_id).execute())

#	def get_input_ids(self):
#		"""Returns list of IDs of inputs currently loaded
#		"""
#		altern_id_list = []
#		for row in self.table.select(order_by=self.table.c.input_id).execute():
#			altern_id_list.append(row.input_id)
#		return altern_id_list
	
	def get_num(self):
		"""Returns the number of inputs stored in the InputSet
		"""
		session = create_session(bind_to=self.metadata.engine)
		return int(session.query(self.mapper).count())

	def __unicode__(self):
		"""Description of object
		"""
		return "<InputSet>"
	
	def __str__(self):
		"""Description of object
		"""
		return "<InputSet>"
	
	def to_string(self):
		"""Returns string representation of the InputSet
		"""
		i = self.table.select().execute()
		ir = i.fetchall()
		input_str = ""
		for row in ir:
			input_str += str(row)+"\n"
		if input_str == "":
			input_str = "No inputs defined"
		return input_str

class Input(object):
    """Input class maps to input DB tables allowing access to them in OO way using SQLAlchemy
    
    Members for this class are created dynamically by SQLAlchemy at the time of mapping.  Member
    names correspond directly to names of attributes in the table mapped to.
    """
    pass
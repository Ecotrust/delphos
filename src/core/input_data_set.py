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
# @summary - 
#===============================================================================

import copy
from sets import Set
from util.common_functions import *
from delphos_exceptions import *

class InputDataSet():
	"""Maintains altern/crit grid input data by the user.
	
	The grid cells of data are represented in a linear list, not a 2D list or other
	The row and column of each cell is stored within the cells structure
	So an 8x8 grid, 8 alternatives, 8 criteria would have a 64 element cell_data list
	
	Ties input values to their associated altern/criteria pair so
	that the user can go back and change the altern and crit without losing
	the data that they already input.  It also separates data from 
	presentation.
	
	input_data: [[[altern_data][crit_data][row][col][value]], ...]
	altern_data: (altern_id, altern_name, altern_color)
	crit_data: (crit_id, crit_name, crit_type, crit_options_units, cost_benefit)
	"""
	
	def __init__(self, altern_data=None, crit_data=None):
		self.num_alterns = 0
		self.num_crits = 0
		self.cell_data = None
		if altern_data and crit_data:	  
			self.cell_data = self.create_cell_data(altern_data, crit_data)
 
	def make_copy(self):
		new_set = InputDataSet()
		new_set.cell_data = copy.copy(self.cell_data)
		new_set.num_alterns = self.num_alterns
		new_set.num_crits = self.num_crits
		return new_set
	
	def create_cell_data(self, altern_data, crit_data):
		cell_data = []
		self.num_alterns = len(altern_data)
		self.num_crits = len(crit_data)
		for i in range(self.num_crits):
			for j in range(self.num_alterns):
				#Append associated alter and crit data to each 'cell'.  
				#Append row and column to put in
				#Append space for input value
				cell_data.append([altern_data[j], crit_data[i], i, j, None])
		
		#print "input data:"
		#print input_data
		
		return cell_data
	
	def update_values(self, new_values):
		for i in range(len(self.cell_data)):
			self.set_value(i, new_values.get_value(i))
	
	def update_headings(self, new_altern_data, new_crit_data):
		if not new_altern_data or not new_crit_data:
			raise Exception, "Error updating input table"
	
		#Create new empty input set
		new_input_data = InputDataSet(new_altern_data, new_crit_data)
		
		#Load values from current input set into new input set where altern 
		#and crit id match
		for i in range(len(self.cell_data)):
			for j in range(len(new_input_data.cell_data)):
				cur_altern_id = self.cell_data[i][0][0]
				cur_crit_id = self.cell_data[i][1][0]
				new_altern_id = new_input_data.cell_data[j][0][0]
				new_crit_id = new_input_data.cell_data[j][1][0]
				if cur_altern_id == new_altern_id and cur_crit_id == new_crit_id:
					#Copy value
					new_input_data.cell_data[j][4] = self.cell_data[i][4]
		
		#Replace current input data set with new updated one
		self.num_alterns = new_input_data.num_alterns
		self.num_crits = new_input_data.num_crits
		self.cell_data = new_input_data.cell_data

	def get_num_alterns(self):
		return self.num_alterns

	def get_num_crits(self):
		return self.num_crits
  
	def get_cell_data(self):
		return self.cell_data
	
	def get_cell_contents(self, index):
		return self.cell_data[index]
	
	def get_num_cells(self):
		return len(self.cell_data)
		
	def get_row(self, index):
		return self.cell_data[index][2]
		
	def get_col(self, index):
		return self.cell_data[index][3]

	def get_value(self, index):
		return self.cell_data[index][4]

	def set_value(self, index, value):
		self.cell_data[index][4] = value

	def get_crit_name(self, index):
		return self.cell_data[index][1][1]
	
	def get_crit_type(self, index):
		return self.cell_data[index][1][2]
	
	def get_altern_name(self, index):
		return self.cell_data[index][0][1]

	def get_qual_rows(self):
		return list(Set([x[2] for x in self.cell_data if x[1][2] == "Ordinal" or x[1][2] == "Binary"]))
	
	def get_quant_rows(self):
		return list(Set([x[2] for x in self.cell_data if x[1][2] == "Ratio"]))

	def check_quant_rows(self):
		"""Check if all rows with quantative criteria have the same values
		within a given row"""
		quant_rows = self.get_quant_rows()
		for row in quant_rows:
			if self.check_same_values_by_row(row):
				crit_name = self.get_crit_name(row)
				raise InputError, unicode(row+1)+" '"+unicode(crit_name)+"'"
		
	def check_qual_rows(self):
		"""Check if all rows with qualitative criteria have the same values
		within a given row"""
		qual_rows = self.get_qual_rows()	   
		row_same_list = []
		for row in qual_rows:		   
			crit_name = self.get_crit_name(row)
			row_same_list.append(self.check_same_values_by_row(row))
			 
		all_same = reduce(lambda x,y: x and y, row_same_list) 
		if all_same: 
			raise InputError, unicode(row+1)+" '"+unicode(crit_name)+"'"
			
	def check_same_values_by_row(self, row):
		"""Check if the cells in any row all have the same values
		"""
		row_cells = self.get_row_cells(row)			
		same_bool_list = [x[4] == y[4] for x in [row_cells[0]] for y in row_cells]
		same = reduce(lambda x, y: x and y, same_bool_list)
		if same:
			return True
		else:
			return False
		
	def get_num_rows(self):
		"""Return number of rows in input data
		"""
		#return list(Set([x[2] for x in self.cell_data]))
		return self.num_crits
	
	def get_row_cells(self, row):
		return [cell for cell in self.cell_data if cell[2] == row]
	
	def get_mca_input(self):
		"""Generate in matrix for Evamix MCA
		alterns down, criteria across, opposite of table widget"""
		input = initialize_int_array(self.get_num_alterns(), self.get_num_crits())
		for cell in self.cell_data:
			col = cell[2] #Note pulling the row valu and using as column
			row = cell[3] #Note pulling the column value and using as row
			input[row][col] = cell[4]
		return input
	
	def load_mca_input(self, input_matrix):
		for cell in self.cell_data:
			col = cell[2]
			row = cell[3]
			cell[4] = input_matrix[row][col]
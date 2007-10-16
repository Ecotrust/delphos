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

class InputWeightSet():
	"""Maintains weights input by the user.
	
	Ties weight values input by user to their associated criterion so
	that the user can go back and change the criteria without losing
	the data that they already input.  It also separates data from 
	presentation.
	"""
	def __init__(self, crit_data):
		#TODO: Really we should only be keeping the id, name and weight
		self.crit_id_column = 0
		self.crit_name_column = 1
		self.weight_column = 2		

		self.weight_data = self.create_weight_data(crit_data)

	def create_weight_data(self, crit_data):
		"""Given a critieria set, create an empty weight set
		"""
		weight_data = []
		for crit in crit_data:
			id = crit[self.crit_id_column]
			name = crit[self.crit_name_column]
			weight_data.append([id, name, None])
		return weight_data
			
	def update_weights(self, new_weights):
		
		if not new_weights or len(new_weights) != len(self.weight_data):
			raise Exception, "Error updating weights"

		#print "Weights before: "
		#print self.get_weight_data()

		#print "New weights: "
		#print new_weights

		for i in range(len(new_weights)):
			self.weight_data[i][self.weight_column] = new_weights[i]
				  
		#print "Update weights"
		#print self.get_weight_data()

	def update_crits(self, new_crit_data):
		#print "New crit data"
		#print new_crit_data
	
		#Create new weight data
		new_weight_data = self.create_weight_data(new_crit_data)
		#Transfer weight values
		for i in range(len(self.weight_data)):	
			for j in range(len(new_weight_data)):
				if new_weight_data[j][self.crit_id_column] == self.weight_data[i][self.crit_id_column]:
					new_weight_data[j][self.weight_column] = self.weight_data[i][self.weight_column]				
		
		#Drop the old weight data
		self.weight_data = new_weight_data
		
		#print "Updated crit data"
		#print self.weight_data
	
	def get_weight_data(self):
		return self.weight_data
	
	def get_weights(self):
		weights = []
		for item in self.weight_data:
			weights.append(item[self.weight_column])
		return weights
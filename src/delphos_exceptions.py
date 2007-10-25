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
# @summary - defines detailed exceptions to use within Delphos
#===============================================================================

class DelphosError(Exception):
	"""The general purpose Delphos exception class.  Use when a more specific exception is not necessary
	"""
	def __init__(self, value=""):
		self.value = value

class InputError(DelphosError):
	"""General purpose exception used for all errors relating to user input
	"""
	pass

class DataImportError(DelphosError):
	"""Exception used for handling errors when inputting alternative/criteria data
	
	Example scenario is the user imports data that is not of the right dimension, an alternative is
	missing.
	"""
	pass
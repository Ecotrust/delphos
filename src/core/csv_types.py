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
# @summary - These classes are used by the Python csv module for parsing 
# structured data files.  Note that the csv module can parse many different 
# types of files, not just comma-delimited ones.
#===============================================================================

import csv

class CSV(csv.excel):
	"""Dialect class defining typical CSV file structure according to Excel
	"""
	pass

class TSV(csv.excel):
	"""Dialect class defining a tab-delimited file structure
	"""
	delimiter = "\t"

csv.register_dialect("CSV",CSV)
csv.register_dialect("TSV",TSV)
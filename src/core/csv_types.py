"""These classes are used by the Python csv module for parsing structured data files.  Note that
the csv module can parse many different types of files, not just comma-delimited ones.
"""

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
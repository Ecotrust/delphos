class DelphosError(Exception):
	"""The general purpose Delphos exception class.  Use when a more specific exception is not necessary
	"""
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class DataImportError(DelphosError):
	"""Exception used for handling errors when inputting alternative/criteria data
	
	Example scenario is the user imports data that is not of the right dimension, an alternative is
	missing.
	"""
	pass
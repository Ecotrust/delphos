from sqlalchemy import *
from delphos_exceptions import *
import os
import sys

class AlternativeSet(object):
	"""Represents a set of alternatives.
	"""
	def __init__(self, name, metadata):
		"""altern_set = AlternativeSet(string, BoundMetadata)
		
		name - name of alternative set and ultimately the underlying DB table
		metadata - SQLAlchemy metadata object providing access to DB engine and tables
		"""
		self.name = name
		self.metadata = metadata
		self.table = None
		self.mapper = None
		
		#Load alternative table from DB if it exists otherwise create it
		if self.metadata.engine.has_table(self.name):
			self.table = Table(self.name, self.metadata, autoload=True)
		else:
			self.__create_alternative_table()
		
		#Map Alternative object to alternative table
		self.mapper = mapper(Alternative, self.table)
		
		#print list(self.table.columns)
		
		#Cross-platform compatible colors taken from 
		#http://www.tbtf.com/resource/20colors.html
		self.default_altern_colors = [
							   	'#ff0000',
							   	'#00ff00',
							   	'#0000ff',
							   	'#ffff00',
							   	'#ff00ff',
							   	'#00ffff',
							   	
								'#000000', 
							   	'#800000', 
							   	'#008000', 
							   	'#808000',
							   	'#000080',
							   	'#800080',
							   	'#008080',
							   	'#c0c0c0',

							   	'#c0dcc0',
							   	'#a6caf0',
							   	'#fffbf0',
							   	'#a0a0a4',
							   	'#808080',
							   	
							   	'#ffffff'
							   	]
		self.extra_color = '#ffffff'

	def __create_alternative_table(self):
		"""Create a new alternative table in the DB
		"""
		self.table = self.__get_alternative_table_object()
		self.table.create()
	
	def __get_alternative_table_object(self):
		"""Create alternative Table object (SQLAlchemy)
		"""
		return Table(self.name, self.metadata,
			Column('alternative_id', Integer, Sequence('altern_id_seq'), primary_key=True),
			Column('name', String(200)),
			Column('color', String(7))
		)
		
	def add_alternative(self, altern_name):
		"""Add alternative to the AlternativeSet
		
		altern_name (string) - name of the alternative
		"""
		#Verify not given duplicate alternative name
		same_list = list(self.table.select(self.table.c.name==altern_name).execute())
		if len(same_list) > 0:
			raise DelphosError, "An alternative named "+str(altern_name)+" already exists in this project."
		else:
			#Get default color
			num_alterns = self.get_num()
			if num_alterns < 20:
				cur_color = self.default_altern_colors[num_alterns]
			else:
				cur_color = self.extra_color
			
			self.table.insert().execute({'name':altern_name, 'color':cur_color})
	
	def remove_alternative_by_id(self, alternative_id):
		"""Remove alternative from AlternativeSet given its unique alternative id
		"""
		result = self.table.delete(self.table.c.alternative_id==alternative_id).execute()
		#TODO : verify this is True
		return True

	def remove_alternative_by_name(self, alternative_name):
		"""Remove alternative from AlternativeSet given its unique alternative id
		"""
		result = self.table.delete(self.table.c.name==alternative_name).execute()
		#TODO : verify this is True
		return True

	def get_all_alternatives(self):
		"""Returns all alternatives in set in list structure [[id, name], ...]
		"""
		return list(self.table.select(order_by=self.table.c.alternative_id).execute())

	def get_alternative_ids(self):
		"""Returns list of IDs of alternatives currently loaded
		"""
		altern_id_list = []
		for row in self.table.select(order_by=self.table.c.alternative_id).execute():
			altern_id_list.append(row.alternative_id)
		return altern_id_list
	
	def get_num(self):
		"""Returns the number of alternatives stored in the AlternativeSet
		"""
		session = create_session(bind_to=self.metadata.engine)
		return int(session.query(self.mapper).count())

	def __unicode__(self):
		"""Description of object
		"""
		return "AlternativeSet"
	
	def __str__(self):
		"""Description of object
		"""
		return "AlternativeSet"
	
	def to_string(self):
		"""Returns string representation of the AlternativeSet
		"""
		i = self.table.select().execute()
		ir = i.fetchall()
		altern_str = ""
		for row in ir:
			altern_str += str(row)+"\n"
		if altern_str == "":
			altern_str = "No alternatives defined"
		return altern_str

class Alternative(object):
	"""Alternative class maps to alternative DB tables allowing access to them in OO way using SQLAlchemy
	
	Members for this class are created dynamically by SQLAlchemy at the time of mapping.  Member
	names correspond directly to names of attributes in the table mapped to.
	"""
	pass
	
#Testing purposes
if __name__ == '__main__':
 	os.chdir('..')	#Go to top-level directory
	db = create_engine('sqlite:///db/project23.del')
	meta = BoundMetaData(db)	#Basically a schema, or table collection
	altern_set = AlternativeSet('alternatives', meta)
	altern_set.add_alternative("testy")
	print altern_set.to_string()
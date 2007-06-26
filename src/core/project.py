import sqlalchemy
import logging
from sqlalchemy import *

class Project():
	def __init__(self, name, path):
		self.name = name
		self.db = None
		self.create_project_db()
		self.create_project_table()

	def create_project_db(self):
		db = create_engine('sqlite:///'+self.path+self.name)
	
	def create_project_table(self):
		crit_table = Table(self.name, metadata,
			Column('criteria_id', Integer, Sequence(self.name+'_id_seq'), primary_key=True),
			Column('description', String(200)),
			Column('type', Integer)
		)
from sqlalchemy import *
import os
import sys

class MCA(object):
    """Handles one multicriteria analysis run.
     
    Handles input data, DB interaction and use of the Evamix algorithm
    """
    def __init__(self, description, metadata):
        """mca_tool = MCA(string, BoundMetadata)
        
        description - describes this particular analysis run
        metadata - SQLAlchemy metadata object providing access to DB engine and tables
        """
        self.metadata = metadata
        self.db_name = db_name
        
        self.table = None
        self.mapper = None
        
        self.__create_analysis_table()

    def __create_analysis_table(self):
        """Create a new input table in the DB
        """
        self.table = self.__get_input_table_object()
        self.table.create()
        #Get creation_date
        #Signal to create analysis record, pass date
    
    def __get_analysis_table_object(self):
        """Create analysis Table object (SQLAlchemy)
        """
        return Table(self.description, self.metadata,
            Column('created', Integer, primary_key=True),
            Column('description', String(200), primary_key=True),
            Column('alternatives', Binary),
            Column('criteria', Binary),
            Column('input_matrix', Binary) 
        )
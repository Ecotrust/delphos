from sqlalchemy import *
import os
import sys
import pickle

class McaRuns(object):
    """Provides access to general project data
    """
    def __init__(self, metadata, db_name):
        """project_data = ProjectData(BoundMetadata, string, string, string)
        
        metadata - SQLAlchemy metadata object providing access to DB engine and tables
        db_name - name to give DB
        project_name - name of project
        type - analaysis type (eg. fisheries or mpa)
        """
        self.metadata = metadata
        self.db_name = db_name
        
        self.table = None
        self.mapper = None
        
        #Load project table from DB if it exists otherwise create it
        if self.metadata.engine.has_table(self.db_name):
            self.table = Table(self.db_name, self.metadata, autoload=True)
        else:
            self.__create_table()
        
        print list(self.table.columns)

    def __create_table(self):
        """Create a new mca runs table in the DB
        """
        self.table = self.__get_table_object()
        self.table.create()
    
    def __get_table_object(self):
        """Create mca runs Table object (SQLAlchemy)
        """
        return Table(self.db_name, self.metadata,
            Column('id', Integer, Sequence('mca_run_seq'), primary_key=True),
            Column('name', Unicode(200)),
            Column('description', Unicode(200)),
            Column('altern_data', Binary()),
            Column('crit_data', Binary()),
            Column('input_data', Binary()),
            Column('input_weights', Binary()),
            Column('results', Binary()),
            Column('created', DateTime(timezone=True))
        )

    def insert(self, name, description, altern_data, crit_data, input_data, input_weights, results):
        print "name: "+name
        print "description: "+description
        
        #TODO: fix altern data to not use a tuple, but lists which are pickleable
        real_altern_data = []
        for row in altern_data:
            real_altern_data.append(list(row))
        altern_data = real_altern_data
            
        altern_data = pickle.dumps(altern_data)
        crit_data = pickle.dumps(crit_data)
        input_data = pickle.dumps(input_data)
        input_weights = pickle.dumps(input_weights)
        results = pickle.dumps(results)
        self.table.insert().execute({'name':unicode(name), 'description':unicode(description), 'altern_data':altern_data, 'crit_data':crit_data, 'input_data':input_data, 'input_weights':input_weights, 'results':results, 'created':func.current_timestamp()})

    def get_all(self):
        """Returns list of mca runs
        """
        rows = self.table.select(order_by=self.table.c.id).execute().fetchall()
        recs = []
        for row in rows:
            cur_row = list(row)
            #unpickle pickled fields
            cur_row[3] = pickle.loads(cur_row[3])
            cur_row[4] = pickle.loads(cur_row[4])
            cur_row[5] = pickle.loads(cur_row[5])
            cur_row[6] = pickle.loads(cur_row[6])
            cur_row[7] = pickle.loads(cur_row[7])
            recs.append(cur_row)
        return recs

    def get_basic(self):
        """Returns list with basic information about analysis runs that have been performed
        """
        rows = self.table.select(order_by=self.table.c.id).execute().fetchall()
        recs = []
        for row in rows:
            cur_row = list(row)
            #Append name, description and date
            recs.append([cur_row[1], cur_row[2], cur_row[8]])
        return recs

    def __unicode__(self):
        """Description of object
        """
        return "MCA runs"
    
    def __str__(self):
        """Description of object
        """
        return "MCA Runs"
    
#Testing purposes
if __name__ == '__main__':
    pass
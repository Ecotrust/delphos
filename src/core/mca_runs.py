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
#===============================================================================

from sqlalchemy import *
import os
import sys
import pickle
from util.common_functions import *

class McaRuns(object):
    """Provides access to MCA input and result data for a given run
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
        
        int_results are intermediate results generated during analysis
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
            Column('created', DateTime(timezone=True)),
            Column('int_results', Binary())
        )

    def insert(self, name, description, altern_data, crit_data, input_data, input_weights, results, int_results):
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
        int_results = pickle.dumps(int_results)
        self.table.insert().execute({'name':unicode(name), 'description':unicode(description), 'altern_data':altern_data, 'crit_data':crit_data, 'input_data':input_data, 'input_weights':input_weights, 'results':results, 'created':func.current_timestamp(), 'int_results':int_results})

    def delete(self, id):
        """Remove mca run given its unique run ID
        """
        result = self.table.delete(self.table.c.id==id).execute()        

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
            cur_row[9] = pickle.loads(cur_row[9])
            recs.append(cur_row)
        return recs
    
    def get_num(self):
        """Returns the number of analysis runs stored
        """
        return len(self.table.select(order_by=self.table.c.id).execute().fetchall())

    def get_basic(self):
        """Returns list with basic information about analysis runs that have been performed
        """
        rows = self.table.select(order_by=self.table.c.id).execute().fetchall()
        recs = []
        for row in rows:
            cur_row = list(row)
            
            #Append name, description and date(local time)
            id = cur_row[0]
            name = cur_row[1]
            description = cur_row[2]
            local_time = utc_to_local_time(cur_row[8])
            recs.append([id, name, description, local_time])
        return recs

    def get_all_by_id(self, id):
        #(altern data, crit data, input data, input weights, results)
        rows = self.table.select(self.table.c.id == id, order_by=self.table.c.id).execute().fetchall()
        for row in rows:
            cur_row = list(row)
            cur_row[3] = pickle.loads(cur_row[3])
            cur_row[4] = pickle.loads(cur_row[4])
            cur_row[5] = pickle.loads(cur_row[5])
            cur_row[6] = pickle.loads(cur_row[6])
            cur_row[7] = pickle.loads(cur_row[7])
            cur_row[9] = pickle.loads(cur_row[9])
            return cur_row

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
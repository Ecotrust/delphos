import logging
from sqlalchemy import *

db = create_engine('sqlite:///project1.db')
metadata = BoundMetaData(db)
#metadata.engine.echo = True

##################### Load Tables Using Reflection #########################

master_alt_table = Table('
messages = Table('messages', meta, autoload = True)

###################### Define Classes ###########################



################# Load Tables With Generated Queries ##################

#Load alternatives
master_alt_table.insert().execute(
	{'name':'Hilsa Fishery'},
	{'name':'Shark Fishery'},
	{'name':'Tamils Mussels'},
	{'name':'Kerala Mussels'},
	{'name':'Babylonia Snail'},
	{'name':'Croacker'},
	{'name':'Oil Sardines'},
	{'name':'Silver Pomfrets'}
)

#Load criteria
master_crit_table.insert().execute(
	{'description':'Fisher\'s current interest to start a certification program' , 'type':3 },
	{'description':'Years for which catch per unit effort data are available', 'type':2 },
	{'description':'Level of understanding of population dynamics', 'type':3 },
	{'description':'Level of community participation in fishery management', 'type':3 },
	{'description':'By catch level', 'type':3 },
	{'description':'Gear ecosystem interactions', 'type':3 }
)

################# Load Tables Using Python Objects  ##################

#Display alternatives
a = master_alt_table.select().execute()
ar = a.fetchall()
for alt in ar:
	print alt

#Display criteria
c = master_crit_table.select().execute()
cr = c.fetchall()
for crit in cr:
	print crit

################### Select Subsets Using Generated SQL ####################

#Select subset of alternatives
sub_alt = master_alt_table.select(
	or_(
		master_alt_table.c.alternative_id==1,
        master_alt_table.c.alternative_id==3,
        master_alt_table.c.alternative_id==6
    )
).execute()

#Select subset of criteria
sub_crit = master_crit_table.select(
	or_(
		master_crit_table.c.criteria_id==1,
        master_crit_table.c.criteria_id==2,
        master_crit_table.c.criteria_id==5
    )
).execute()

#Get results
alt_res = sub_alt.fetchall()
crit_res = sub_crit.fetchall()

#################### Populate Input Table Using Subselect Results ############

#Populate new input table
for sub_alt in alt_res:
	for sub_crit in crit_res:
		input_table.insert().execute({'alternative_id':sub_alt.alternative_id, 'criteria_id':sub_crit.criteria_id, 'value':4})
		
i = input_table.select().execute()
ir = i.fetchall()
for input in ir:
	print input

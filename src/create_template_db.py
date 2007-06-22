import logging
from sqlalchemy import *

db = create_engine('sqlite:///db/template.db')
metadata = BoundMetaData(db)
metadata.engine.echo = True

##################### Define Tables #########################

#Define alternative table
alt_table = Table('alternatives', metadata,
	Column('alternative_id', Integer, Sequence('alt_id_seq'), primary_key=True),
	Column('name', String(50))
)

#Define criteria table
crit_table = Table('criteria', metadata,
	Column('criteria_id', Integer, Sequence('crit_id_seq'), primary_key=True),
	Column('description', String(200)),
	Column('type', Integer)
)

#Define input table
alt_crit_input_table = Table('alt_crit_input', metadata,
	Column('alternative_id', Integer, ForeignKey('alternatives.alternative_id')),
	Column('criteria_id', Integer, ForeignKey('criteria.criteria_id')),
	Column('value', Integer)
)

crit_table.create()
alt_table.create()
alt_crit_input_table.create()
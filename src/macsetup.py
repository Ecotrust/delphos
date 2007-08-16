#from setuptools import setup
from distutils.core import setup
import py2app
import glob

#In order to make matplotlib bundle correctly, need to add pytz 
#package using easty_install or other, add empty __init__.py file 
#to zoneinfo subdir, move aside pytz/zoneinfo/UTC and create an 
#empty pytz/zoneinfo/UTC.py file Somewhere in your code add 
#'import pytz.zoneinfo' so py2app will pick up the package.  
#Very broken method but it works.  I have no intention of using 
#the zoneinfo stuff

# Build the .app file
setup(
	options=dict(
		py2app=dict(
			argv_emulation=1,
			optimize=2,
			site_packages=True,
			includes="FileDialog, Tkinter, numpy, sqlalchemy,sqlalchemy.*,sqlalchemy.mods.*,sqlalchemy.databases.*,sqlalchemy.engine.*,sqlalchemy.ext.*,sqlalchemy.orm.*"
		),
	),
	app=[ 'start_gui.py' ],
	install_requires=['py2app','SQLAlchemy','numpy']
)

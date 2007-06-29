#from setuptools import setup
from distutils.core import setup
import py2app
import glob

# Build the .app file
setup(
	options=dict(
		py2app=dict(
			argv_emulation=1,
			optimize=2,
			site_packages=True,
			includes="sqlalchemy,sqlalchemy.*,sqlalchemy.mods.*,sqlalchemy.databases.*,sqlalchemy.engine.*,sqlalchemy.ext.*,sqlalchemy.orm.*"
		),
	),
	app=[ 'start_delphos.py' ],
	install_requires=['py2app','SQLAlchemy']
)

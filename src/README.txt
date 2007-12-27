===================
Open Delphos Readme
===================

Open Delphos is designed to provide a complete solution for performing 
multi-criteria analysis (MCA).  It is cross-platform and able to run on
Linux, Mac OSX and Windows.

Open Delphos Homepage: 
http://trac.infodrizzle.org/opendelphos/

============
Requirements
============

Open Delphos is known to work with Python 4.2.3 and later

Python Modules required:
  - QT 4.2
  - PyQT
  - SIP
  - SQLAlchemy
  - PyExcelerator
  - SQLite (Already built into Python 2.5)

Running Open Delphos from source:
  - Run make from the src directory to build all of the PyQT interfaces
  - Run start_gui.py

Building Open Delphos into a standalone application

  Additional packages needed for compiling a standalone Delphos executable:
  - py2app (Max OS X)
  - py2exe (Windows)
  
  Max OSX
  >python macsetup.py py2app
  - app will be in the dist directory
  
  Windows
  >python winsetup.py py2exe
  - executable will be in the dist directory
  - the db and data directories will need to be copied to where the 
	executable is located (needs to be automated in future)

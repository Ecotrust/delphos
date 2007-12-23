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
# $Id: start_gui.py 80 2007-10-12 03:50:12Z timw 
#
# @summary - configuration file for py2exe.  Used to build a standalone
# executable version of Delphos
# 
# @warning - In order to make matplotlib bundle correctly, need to add pytz 
# package using easty_install or other, add empty __init__.py file 
# to zoneinfo subdir, move aside pytz/zoneinfo/UTC and create an 
# empty pytz/zoneinfo/UTC.py file Somewhere in your code add 
# 'import pytz.zoneinfo' so py2app will pick up the package.  
# Very broken method but it works.  I have no intention of using 
# the zoneinfo stuff
#===============================================================================

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
			includes="FileDialog, Tkinter, numpy, sqlalchemy,sqlalchemy.*,sqlalchemy.mods.*,sqlalchemy.databases.*,sqlalchemy.engine.*,sqlalchemy.ext.*,sqlalchemy.orm.*"
		),
	),
	app=[ 'Delphos.py' ],
	install_requires=['py2app','SQLAlchemy','numpy']
)

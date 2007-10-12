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
#
# @summary - configuration file for py2exe.  Used to build a standalone
# executable version of Delphos
#===============================================================================

from py2exe.build_exe import py2exe
from distutils.core import setup

import matplotlib

opts = {
	"py2exe": {
		"includes": [],
	"excludes": ['backend_gtkagg', 'backend_wxagg'],
	"dll_excludes": ['libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk-win32-2.0-0.dll'],
		"packages": ["sqlalchemy", "pyExcelerator", "matplotlib", "pytz"],
		"dist_dir": "bin",
	}
}
 
setup(options = opts,
	  console=[{"script": "start_gui.py"}],
	  data_files=[matplotlib.get_py2exe_datafiles()]
)

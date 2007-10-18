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
# @summary - Top level script used to start the delphos application
#===============================================================================

#Built-in modules
import sys

#Third-party modules
import sip
import pyExcelerator
import sqlalchemy
from pyExcelerator import *
from sqlite3 import dbapi2 as sqlite

#Delphos modules
from core.project_manager import *
from core.config_manager import *
from gui.gui_manager import *

if __name__ == "__main__":
	project_manager = ProjectManager()
	config_manager = ConfigManager()
	gui_manager = GuiManager(project_manager, config_manager)
	gui_manager.start_gui()
#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
#
# @license - This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# $Id$
#===============================================================================

#Built-in modules
import sys

#Third-party modules
import sip
import pyExcelerator
import sqlalchemy
from pyExcelerator import *

#Delphos modules
from core.project_manager import *
from gui.gui_manager import *

if __name__ == "__main__":
	project_manager = ProjectManager()
	gui_manager = GuiManager(project_manager)
	gui_manager.start_gui()
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
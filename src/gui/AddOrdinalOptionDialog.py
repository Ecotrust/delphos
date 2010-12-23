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
# @summary - 
#===============================================================================

import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from add_ordinal_option_ui import Ui_AddOrdinalOptionDialog

class AddOrdinalOptionDialog(QDialog, Ui_AddOrdinalOptionDialog):
    """Manages the add alternative dialog
    """
    def __init__(self, gui_manager, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.gui_manager = gui_manager
        self.isError = False	#Error flag for form processing
        self.errorMsg = ""
        QObject.connect(self.add_ordinal_option_box,QtCore.SIGNAL("accepted()"), self.process_accept)
        self.retranslate() #Translate the text
        
    def process_accept(self):
        """Processes clicking of OK button in dialog
        """
        self.errorMsg = ""
        option_info = None
        
        option_description = self.option_description_edit.text()
        if not option_description:
            self.isError = True
            self.errorMsg += self.option_error
        
        option_value = self.option_value_edit.text()
        if not option_value:
            self.isError = True
            self.errorMsg += self.rank_error
        else:
            try:
                option_value = int(option_value)
            except:
                self.isError = True
                self.errorMsg += self.rank_int_error

            if option_value < 1 and not self.isError:
                self.isError = True
                self.errorMsg += self.pos_int_error+unicode(option_value)

        if self.isError:
            self.isError = False
            QMessageBox.critical(self,self.ord_add_error,self.errorMsg)
        else:
            option_info = (option_description, option_value)
            self.emit(SIGNAL("ordinal_option_info_collected"), option_info)
            
    def retranslate(self):
        #Example self. = QApplication.translate("AddOrdinalOptionDialog", "english_text", "description", QApplication.UnicodeUTF8)                    
        self.option_error = QApplication.translate("AddOrdinalOptionDialog", "* Please enter an option description.\n", "Error when no description provided for option", QApplication.UnicodeUTF8)                           
        self.rank_error = QApplication.translate("AddOrdinalOptionDialog", "* Please enter an option rank.\n", "Error when no rank provided", QApplication.UnicodeUTF8)                            
        self.rank_int_error = QApplication.translate("AddOrdinalOptionDialog", "* Option rank is not an integer", "Error when rank is not an integer", QApplication.UnicodeUTF8)                            
        self.pos_int_error = QApplication.translate("AddOrdinalOptionDialog", "* Option rank must be a positive integer greater than zero, you entered ", "Error when rank is not greater than zero", QApplication.UnicodeUTF8) 
        self.ord_add_error = QApplication.translate("AddOrdinalOptionDialog", "Error adding ordinal criteria option", "Error when option is not added properly", QApplication.UnicodeUTF8) 
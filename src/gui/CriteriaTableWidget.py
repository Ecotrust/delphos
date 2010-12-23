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

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from delphos_exceptions import *

class CriteriaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)
        self.retranslate() #Translate UI text

    def load(self, criteria_recs):
        """Loads the table in the criteria tab with the existing project criteria
        """
        if criteria_recs:
            self.clearContents()
            self.setRowCount(len(criteria_recs))        
            for i in range(len(criteria_recs)):                
                if i == 0:
                    hi = self.horizontalHeaderItem(0)
                    hi.setToolTip(self.desc_header)
                    hi = self.horizontalHeaderItem(1)
                    hi.setToolTip(self.crit_type_header)
                    hi = self.horizontalHeaderItem(2)
                    hi.setToolTip(self.options_header)
                    hi = self.horizontalHeaderItem(3)
                    hi.setToolTip(self.b_or_c_header)
                                        
                name_val = unicode(criteria_recs[i][1])
                type_val = unicode(criteria_recs[i][2])
                type_opt_val = u""
                if type_val == 'Ordinal' or type_val == 'Binary':
                    for opt in criteria_recs[i][3]:
                        type_opt_val += u"("+opt[0]+u": "+unicode(opt[1])+u")"
                cb_val = unicode(criteria_recs[i][4])
                
                #print name_val
                #print type_val
                #print type_opt_val
                #print cb_val
                
                name_item = QTableWidgetItem()
                name_item.setText(name_val)
                self.setItem(i, 0, name_item)
    
                type_item = QTableWidgetItem()
                type_item.setText(type_val)
                self.setItem(i, 1, type_item)
    
                type_opt_item = QTableWidgetItem()
                type_opt_item.setText(type_opt_val)
                self.setItem(i, 2, type_opt_item)
    
                cb_item = QTableWidgetItem()
                cb_item.setText(cb_val)
                self.setItem(i, 3, cb_item)

                self.resizeColumnsToContents()

    def get_selected_row_indexes(self):
        model = self.selectionModel()
        indexes = model.selectedRows(0)
        if indexes:
            #Return the unique criteria description
            return indexes
        else:
            raise DelphosError, self.no_crit_error

    def get_first_selected_row_item(self):
        selected_row = self.selectedItems() 
        if selected_row:
            return selected_row[0]  
        else:
            raise DelphosError, self.no_crit_error

    def retranslate(self):
        #Example self. = QApplicationpplication.translate("CriteriaTableWidget", "english_text", "description", QApplication.UnicodeUTF8)                    
        self.desc_header = QApplicationpplication.translate("CriteriaTableWidget", "Description - this column provides a detailed explanation of the criterion", "Explanation of how to interpret the 'description' criteria table column", QApplication.UnicodeUTF8)                            
        self.crit_type_header = QApplicationpplication.translate("CriteriaTableWidget", "Criteria Type - this column gives you the overall type of the criterion.  Possible types include: Binary, Ordinal or Ratio\nClick help icon for more information", "Explanation of how to interpret 'criteria type' table column", QApplication.UnicodeUTF8)                            
        self.options_header = QApplicationpplication.translate("CriteriaTableWidget", "Options/Units - for Binary or Ordinal criterion this column will give you the list of available options to answer with.\n  For Ratio criteria this column will give you the unit of measure that answers must be in.  For example 'tons per year' or 'pounds',", "Explanation of how to interpret 'options/units' crit table column", QApplication.UnicodeUTF8)                           
        self.b_or_c_header = QApplicationpplication.translate("CriteriaTableWidget", "Benefit/Cost - Tells you whether the criterion is a Benefit (positive) or a Cost (negative).  Click the help icon for more information", "Explanation of the 'cost/benefit' crit table column", QApplication.UnicodeUTF8)                    
        self.no_crit_error = QApplicationpplication.translate("You must first select a criterion", "Error when a crit was not selected", QApplication.UnicodeUTF8)                    
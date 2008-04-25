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
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from core.input_data_set import *
from core.input_weight_set import *
from mca_result_view_ui import Ui_McaResultView

from util.common_functions import *

class McaResultView(QDialog, Ui_McaResultView):
    """Manages the viewing of MCA analysis results
    """
    def __init__(self, gui_manager, parent, project):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.project = project
        self.gui_manager = gui_manager
        self.isError = False    #Error flag for form processing
        self.errorMsg = ""
        
        self.altern_color_column = 2
        
    def load_results(self, name, description, altern_data, crit_data, input_data, input_weights, results):        

        self.setWindowTitle(name)

        self.altern_table.load(altern_data)
        self.crit_table.load(crit_data)

        input_weight_set = InputWeightSet(crit_data)
        input_weight_set.update_weights(input_weights)
        self.weight_table.load(input_weight_set)
        
        input_data_set = InputDataSet(altern_data, crit_data)
        input_data_set.load_mca_input(input_data)
        self.input_table.load(input_data_set)

        interm_results = {}
        #Build results dictionary using altern id as key

        for i in range(len(results)):
            (altern_id, altern_name, altern_color) = altern_data[i]
            score = results[i]
            interm_results[altern_id] = score

        #Sort alterns by score
        from operator import itemgetter
        sorted_results = sorted(interm_results.items(), key=itemgetter(1), reverse=True)
        
        #Make altern recs a dict using altern_id as key
        altern_dict = {}
        for altern in altern_data:
            altern_dict[altern[0]] = altern[1]

        #Build results list using altern id as key
        final_results = initialize_list(len(results), None)
        final_sorted = initialize_list(len(results), None)
        rank = None
        prev_s_score = None
        print sorted_results
        
        for i in range(len(sorted_results)):
            #Get current score in sorted list
            (s_altern_id, s_score) = sorted_results[i]
            #Get previous score in sorted list, if there is one
            if i > 0:
                prev_s_score = sorted_results[i-1][1]
            else:
                prev_s_score = None
            
            for j in range(len(results)):
                (altern_id, altern_name, altern_color) = altern_data[j]
                score = interm_results[altern_id]
                altern_name = altern_dict[altern_id]
                altern_color = altern_data[j][self.altern_color_column]
                
                if s_altern_id == altern_id:
                    if score == prev_s_score:
                        break
                    else:
                    	if not rank:
                    		rank = 1
                    	else:
                        	rank += 1
                        break

            #original order                
            final_results[j] = [altern_id, altern_name, rank, round(score,2), altern_color]
            #ordered by rank
            final_sorted[i] = [altern_id, altern_name, rank, round(score,2), altern_color]

        print final_sorted            
        self.final_table.load(final_sorted)
        self.mca_plot_canvas.draw_bar_chart(final_sorted)
        #self.mca_plot_canvas.compute_initial_figure()
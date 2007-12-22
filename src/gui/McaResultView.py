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

        from operator import itemgetter
        sorted_results = sorted(interm_results.items(), key=itemgetter(1), reverse=False)
        
        #Make altern recs a dict using altern_id as key
        altern_dict = {}
        for altern in altern_data:
            altern_dict[altern[0]] = altern[1]

        final_results = []

        #Build results dictionary using altern id as key
        last_rank = None
        last_score = None
        for i in range(len(results)):
            (altern_id, altern_name, altern_color) = altern_data[i]
            score = round(interm_results[altern_id], 4)
            altern_name = altern_dict[altern_id]
            altern_color = altern_data[i][self.altern_color_column]
            
            rank = None
            for j in range(len(sorted_results)):
                (s_altern_id, s_score) = sorted_results[j]
                if s_altern_id == altern_id:
                    if last_score == score:
                        if last_rank == None:
                            last_rank = 1
                            
                        rank = last_rank
                    else:
                        if last_rank == None:
                            last_rank = 0
                            
                        rank = last_rank+1
                        last_rank += 1
                        
                    last_score = score
                
            final_results.append([altern_id, altern_name, rank, score, altern_color])
        
        self.final_table.load(final_results)
        self.mca_plot_canvas.draw_bar_chart(final_results)
        #self.mca_plot_canvas.compute_initial_figure()
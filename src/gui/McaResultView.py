import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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
        
    def load_results(self, name, description, altern_data, crit_data, input_data, input_weights, results):        
        final_results = {}
        #Build results dictionary using altern id as key
        for i in range(len(results)):
            (altern_id, altern_name, altern_color) = altern_data[i]
            score = results[i]
            final_results[altern_id] = score
            
        from operator import itemgetter
        sorted_results = sorted(final_results.items(), key=itemgetter(1), reverse=True)
        


        #Make altern recs a dict using altern_id as key
        altern_dict = {}
        for altern in altern_recs:
            altern_dict[altern[0]] = altern[1]


        final_data = []
        for i in range(len(sorted_results)):
            (altern_id, score) = sorted_results[i]
            score = round(score, 4)
            altern_name = altern_dict[altern_id]
            final_data.append([altern_id, altern_name, rank, score])

        
        self.final_table.load(altern_data, sorted_results)
        self.mca_plot_canvas.draw_bar_chart(altern_data, results)
        #self.mca_plot_canvas.compute_initial_figure()
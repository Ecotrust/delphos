#!/usr/bin/env python

# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

import sys, os, random
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from pylab import * #Keep
import pytz.zoneinfo #Keep
from pytz.zoneinfo import UTC #Keep

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)

class McaMplCanvas(MyMplCanvas):
    
    def draw_bar_chart(self, altern_data, scores):
        altern_names = []
        altern_colors = []
        for row in altern_data:
            altern_names.append(row[1])    #append alternative name
            altern_colors.append(row[2])
        
        N = len(scores)
        nums = range(1, N+1)
        ind = arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        #Random array of RGB tuples
        
        #colors = range(len(scores))
        #colors = [rand(3) for x in colors]

        #pure matplotlib figure
        p1 = bar(ind, scores, width, color=altern_colors, edgecolor='k')
        #pyqt matplotlib widget
        self.axes.bar(ind, scores, width, color=altern_colors)
        self.axes.legend(p1, altern_names, loc='best', pad=0.1, prop=FontProperties(size='small'))
        
        ylabel('Scores')
        title('MCA Results')
        legend(p1, altern_names, loc='best', pad=0.1, prop=FontProperties(size='small'))
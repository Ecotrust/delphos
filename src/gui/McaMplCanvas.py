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

import sys, os, random
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from pylab import * #Keep
#import pytz.zoneinfo #Keep
#from pytz.zoneinfo import UTC #Keep

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
    
    def draw_bar_chart(self, final_results):
        altern_names = []
        altern_colors = []
        scores = []
        ranks = []
        for row in final_results:
            altern_names.append(row[1])    #append alternative name
            altern_colors.append(row[4])
            scores.append(row[3])
            ranks.append(row[2])
            
        N = len(scores)
        nums = range(1, N+1)
        ind = arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        #Random array of RGB tuples
        
        #colors = range(len(scores))
        #colors = [rand(3) for x in colors]

        #pure matplotlib figure
        print ind
        print ranks
        print scores
        
        p1 = bar(range(len(scores)), scores, width, color=altern_colors, edgecolor='k')

        #pyqt matplotlib widget (subplot)
        self.axes.bar(range(len(scores)), scores, width, color=altern_colors)
        #Y-axis ticks should be whole integers
        majorLocator = MultipleLocator(1)
        self.axes.xaxis.set_major_locator(majorLocator)
        #self.axes.yaxis.set_major_locator(majorLocator)
        #X-axis should have no ticks
        self.axes.xaxis.set_major_locator(NullLocator())
        #self.axes.legend(p1, altern_names, 'best', pad=0.1, prop=FontProperties(size='small'))
#       self.axes.set_title ('MCA Results', va='top')
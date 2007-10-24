#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright    2007 Ecotrust
# @author        Tim Welch
# @contact        twelch at ecotrust dot org
# @license        GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id$
#===============================================================================

import os
import time
import codecs

class DelphosLog():
    def __init__(self):
        self.f = codecs.open(os.getcwd()+os.sep+"error.log", 'a', 'utf-8')
        
    def write(self, text):
        time_str = time.strftime("%-%m-%d %H:%M:%S")
        self.f.write(u'\n'+unicode(time_str)+u"\n")
        self.f.write(unicode(text))
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
#
# @summary - evamix algorithm unit tests
#===============================================================================

import unittest
from evamix import Evamix
from delphos_exceptions import *

class TestEvamix(unittest.TestCase):
    
    def setUp(self):
        self.evamix = Evamix()

    def test_bad_input(self):
        """test_bad_input - tests various types of bad input to do_analysis method
        """
        #India 1 input
        input = [
            [4, 3, 4, 2, 4, 3, 3, 2, 2, 2, 3, 4, 2, 1, 1, 3, 2, 3, 37900, 0],
            [3, 2, 3, 3, 4, 2, 3, 2, 2, 2, 3, 4, 3, 2, 1, 3, 3, 3, 3000, 15000],
            [3, 3, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 240, 256],
            [4, 4, 3, 4, 3, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 12231, 5000],
            [2, 2, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 3, 1, 25, 700],
            [3, 3, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 2, 1, 1, 3, 3, 3, 19700, 15700],
            [3, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 3, 1, 1, 3, 2, 3, 119648, 300],
            [3, 2, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 3, 1, 1, 3, 3, 3, 14875, 15700]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]

        #wrong type for input matrix
        self.assertRaises(Exception, self.evamix.do_analysis, "", crit_weights, crit_types)
        self.assertRaises(Exception, self.evamix.do_analysis, None, crit_weights, crit_types)
        #wrong type for input matrix
        self.assertRaises(Exception, self.evamix.do_analysis, input, "", crit_types)
        self.assertRaises(Exception, self.evamix.do_analysis, input, None, crit_types)
        #number of alternatives and weightings don't match

    def test_weight_standardizing(self):
        """test_weight_standardizing - Verify weights add up to 1 after being standardized
        """
        #India 1 input
        input = [
            [4, 3, 4, 2, 4, 3, 3, 2, 2, 2, 3, 4, 2, 1, 1, 3, 2, 3, 37900, 0],
            [3, 2, 3, 3, 4, 2, 3, 2, 2, 2, 3, 4, 3, 2, 1, 3, 3, 3, 3000, 15000],
            [3, 3, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 240, 256],
            [4, 4, 3, 4, 3, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 12231, 5000],
            [2, 2, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 3, 1, 25, 700],
            [3, 3, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 2, 1, 1, 3, 3, 3, 19700, 15700],
            [3, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 3, 1, 1, 3, 2, 3, 119648, 300],
            [3, 2, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 3, 1, 1, 3, 3, 3, 14875, 15700]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]

        self.evamix.standardize_weights(crit_weights)
        self.assertAlmostEqual(sum(crit_weights), 1.0, 6)
    
    def test_all_qual_crit_values_equal(self):
        """test_all_qual_crit_values_equal. Tests input of same qualitative value for each criteria for each alternative
        """
        input = [
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 1, 8],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 2, 7],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 6],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 4, 5],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 5, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 6, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 67, 2],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 7, 43]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]

        self.assertRaises(DelphosError, self.evamix.do_analysis, input, crit_weights, crit_types)

    def test_all_quant_crit_values_equal(self):
        """test_all_quant_crit_values_equal - Tests input of same quantitative value for each criteria for each alternative
        """
        input = [
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]
        self.assertRaises(DelphosError, self.evamix.do_analysis, input, crit_weights, crit_types)

    def test_one_quant_crit_values_equal(self):
        """test_one_quant_crit_values_equal - Tests input of same value for one quantitative criterion for all alternatives
        """
        input = [
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 2],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 5],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 6],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 7],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 3, 8]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]
        self.assertRaises(DelphosError, self.evamix.do_analysis, input, crit_weights, crit_types)

    def test_one_qual_crit_values_equal(self):
        """test_one_qual_crit_values_equal - Tests input same value for one qual criterion for all alternatives
        """
        input = [
            [4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 4, 1],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 5, 1],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 6, 1],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 7, 1],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 8, 2],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 5, 2],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4, 4, 2]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]

        self.evamix.do_analysis(input, crit_weights, crit_types)
        #self.assertRaises(DelphosError, self.evamix.do_analysis, input, crit_weights, crit_types)
    
    def test_all_qual_criteria(self):
        """test_all_qual_criteria - Input all qualitative criteria
        """
        input = [
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 1, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 4],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        crit_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal"]
        self.evamix.do_analysis(input, crit_weights, crit_types)

    def test_all_quant_criteria(self):
        """test_all_quant_criteria - Input all quantitative critera
        """
        input = [
            [2,9],
            [3,8],
            [4,7],
            [5,6],
            [6,5],
            [7,5],
            [8,4],
            [9,3]
        ]
        crit_weights = [1, 1]
        crit_types = ["Ratio","Ratio"]
        self.evamix.do_analysis(input, crit_weights, crit_types)
        
    def test_correct_output_1(self):
        """test_correct_output_1 - Test correct output from Evamix to 6 decimal places for known good inputs
        """
        #India 1 input
        input = [
            [4, 3, 4, 2, 4, 3, 3, 2, 2, 2, 3, 4, 2, 1, 1, 3, 2, 3, 37900, 0],
            [3, 2, 3, 3, 4, 2, 3, 2, 2, 2, 3, 4, 3, 2, 1, 3, 3, 3, 3000, 15000],
            [3, 3, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 240, 256],
            [4, 4, 3, 4, 3, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 12231, 5000],
            [2, 2, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 3, 1, 25, 700],
            [3, 3, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 2, 1, 1, 3, 3, 3, 19700, 15700],
            [3, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 3, 1, 1, 3, 2, 3, 119648, 300],
            [3, 2, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 3, 1, 1, 3, 3, 3, 14875, 15700]
        ]
        #Equal weighting
        crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]
        #Expected output based on Evamix spreadsheet
        expected_result = [0.012674824114427198, 0.0045984415393091494, 0.11013773780133171, 0.16730015203740953, 0.0080016073836221453, -0.055848488243838805, -0.17677788526299262, -0.070086389369268295]
        result = self.evamix.do_analysis(input, crit_weights, crit_types)
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected_result[i], 6)

    def test_correct_output_2(self):
        """test_correct_output_2 - Test correct output for known good input
        """
        #India 1 input
        input = [
            [4, 3, 4, 2, 4, 3, 3, 2, 2, 2, 3, 4, 2, 1, 1, 3, 2, 3, 37900, 0],
            [3, 2, 3, 3, 4, 2, 3, 2, 2, 2, 3, 4, 3, 2, 1, 3, 3, 3, 3000, 15000],
            [3, 3, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 240, 256],
            [4, 4, 3, 4, 3, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 2, 3, 12231, 5000],
            [2, 2, 3, 4, 4, 4, 3, 4, 2, 2, 2, 4, 4, 1, 1, 3, 3, 1, 25, 700],
            [3, 3, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 2, 1, 1, 3, 3, 3, 19700, 15700],
            [3, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 3, 1, 1, 3, 2, 3, 119648, 300],
            [3, 2, 3, 2, 2, 3, 1, 2, 2, 3, 3, 4, 3, 1, 1, 3, 3, 3, 14875, 15700]
        ]
        #Equal weighting
        #crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
        crit_weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]
        #Expected output based on Evamix spreadsheet
        expected_result = [0.0228824278,0.0393816192,0.095598064,.1487528546,0.0161194637,-0.0546693841,-.2000641341,-0.0680009111]
        self.evamix.debug = True
        result = self.evamix.do_analysis(input, crit_weights, crit_types)
        self.evamix.debug = False
        print result
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected_result[i], 6)
        
if __name__ == '__main__':
    unittest.main()
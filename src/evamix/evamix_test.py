import unittest
from evamix import Evamix

class TestEvamix(unittest.TestCase):
    
    def setUp(self):
        self.evamix = Evamix()
        #India 1 input
        self.input = [
            [4,3,3,4,2,3,3,3],
            [3,2,3,4,2,3,3,2],
            [4,3,3,3,3,3,2,3],
            [2,3,4,4,4,2,2,2],
            [4,4,4,3,4,2,2,2],
            [3,2,4,4,4,3,3,3],
            [3,3,3,3,3,1,2,1],
            [2,2,4,4,4,2,2,2],
            [2,2,2,2,2,2,2,2],
            [2,2,2,2,2,3,2,3],
            [3,3,2,2,2,3,2,3],
            [4,4,4,4,4,4,4,4],
            [2,3,4,4,4,2,3,3],
            [1,2,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [3,3,3,3,3,3,3,3],
            [2,3,2,2,3,3,2,3],
            [3,3,3,3,1,3,3,3],
            [37900,3000,240,12231,25,19700,119648,14875],
            [0,15000,256,5000,700,15700,300,15700],
        ]
        #Equal weighting
        self.crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]

    def test_bad_input(self):
        #wrong type for input matrix
        self.assertRaises(Exception, self.evamix.do_analysis, "", self.crit_weights)
        self.assertRaises(Exception, self.evamix.do_analysis, None, self.crit_weights)
        #wrong type for input matrix
        self.assertRaises(Exception, self.evamix.do_analysis, self.input, "")
        self.assertRaises(Exception, self.evamix.do_analysis, self.input, None)
        #number of alternatives and weightings don't match

    def test_weight_standardizing(self):
        self.evamix.standardize_weights(self.crit_weights)
        self.assertAlmostEqual(sum(self.crit_weights), 1.0, 6)

if __name__ == '__main__':
    unittest.main()
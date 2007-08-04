from delphos_exceptions import *
import csv
from copy import deepcopy

#dialect class defining structure of files we'll be parsing
class TSV(csv.excel):
    delimiter = "\t"
csv.register_dialect("TSV",TSV)

class Evamix(object):
    
    def __init__(self):
        pass

    def do_analysis(self, in_matrix, crit_weights, crit_types):
        """Performs multicriteria analysis using the Evamix algorithm
        """
        if not in_matrix:
            raise DelphosError, "No in_matrix matrix"
        if type(in_matrix) is not type([]):
            raise DelphosError, "Bad in_matrix matrix"
        if not crit_weights:
            raise DelphosError, "No criteria weights given"
        if type(crit_weights) is not type([]):
            raise DelphosError, "Expected list of crit_weights"
        if not crit_types:
            raise DelphosError, "No criteria types given"
        if type(crit_types) is not type([]):
            raise DelphosError, "No criteria types given"
    
        if len(in_matrix) < 1:
            raise DelphosError, "in_matrix contains no data"
        
        num_alterns = len(in_matrix[0])
        num_crit_weights = len(crit_weights)
        if num_alterns is not num_crit_weights:
            raise DelphosError, "Number of alternatives in in_matrix ("+str(num_alterns)+") does not match number of crit_weights given ("+str(num_crit_weights)+")"
        
        #Get lists describing which columns (criteria) in in_matrix are quantitative and which are qualitative
        (quant_cols, qual_cols) = self.gen_crit_type_lists(crit_types)
        print "\nquant columns:"
        print quant_cols
        print "\nqual columns:"
        print qual_cols
        
        #Standardize weights
        self.standardize_weights(crit_weights)
        print "\nstandardized weights: "
        print crit_weights
        in_matrix = self.standardize_quantitative_values(in_matrix, quant_cols)
        print "\nstandardized quant values"
        for row in in_matrix:
            print row
    
        #Generate quantitative impact matrix
        quant_impact_matrix = self.gen_quant_impact_matrix(in_matrix, crit_weights, quant_cols)
        print "\nquant impact matrix:"
        for row in quant_impact_matrix:
            print row

        #Compute absolute value of quantitative impact matrix
        quant_impact_abs = self.absolute(quant_impact_matrix)
        print "quantitative impact matrix"
        print quant_impact_abs

        #Generate quantitative final matrix
        #quant_final_matrix = self.gen_quant_final_matrix() 
        
        #Generate qualitative impact matrix
        #qual_impact_matrix = self.gen_qual_impact_matrix(in_matrix, crit_weights, qual_cols)
        
        #Generate qualitative impact matrix
        
    def gen_crit_type_lists(self, crit_types):
        """Given a list of criteria types (eg. "Binary", "Ordinal", "Ratio"), 
        returns a tuple containing two lists. 1 of indices of quantitative 
        criteria and 1 of indices of qualitative criteria.  These are indices 
        into the crit_types (or in_matrix) list allowing for quick retrieval 
        of criteria of one type or the other during the analysis process.
        """   
        quant_list = []
        qual_list = []
        for i in range(len(crit_types)):
            cur_type = crit_types[i]
            if cur_type is "Ratio":
                quant_list.append(i)
            elif cur_type is "Ordinal" or cur_type is "Ratio":
                qual_list.append(i)
        return (quant_list, qual_list)

    def standardize_weights(self, weights):
        """Standardizes a set of criteria weights, modifies the list given, returns nothing
    
        The higher the weight value the less important it is, the lower its 
        standardized weight score will be.  The set of standardized scores sum to 1.
        """
        max_weight = max(weights)
        new_weights = []
        std_weights = []
        
        for i in range(len(weights)):
            new_weight = (weights[i]*-1)+max_weight+1
            new_weights.append(new_weight)
        new_sum = sum(new_weights)
        
        for i in range(len(new_weights)):
            weight = new_weights[i]
            std_weight = float(weight)/float(new_sum)
            weights[i] = std_weight

    def standardize_quantitative_values(self, in_matrix, quant_cols):
        """Standardizes all quantitative values.
        
        Return a 2D list which is in_matrix with just the quant values modified"""
        #Copy in_matrix, each iteration needs the untouched original.
        new_matrix = deepcopy(in_matrix)
        #Go right to the quantitative columns for each alternative
        for i in range(len(in_matrix)):
            for j in quant_cols:
                #Get all values for current quant column
                crit_vals = self.get_criteria_by_col(in_matrix, j)                    
                val = in_matrix[i][j]
                min_val = min(crit_vals)
                max_val = max(crit_vals)
                val = float(val-min_val)/float(max_val-min_val)
                new_matrix[i][j] = val
        return new_matrix

    def get_criteria_by_col(self, in_matrix, col):
        """Traverses in_matrix horizontally getting a list of values for the given column""" 
        col_vals = []
        for i in range(len(in_matrix)):
            col_vals.append(in_matrix[i][col])
        return col_vals

    def gen_quant_impact_matrix(self, in_matrix, crit_weights, quant_cols):
        """Construct pair-wise impact matrix
        
        Compares quantitative criteria for each alternative"""
        dim = len(in_matrix)
        mat = self.initialize_array(dim, dim)
        #Pair-wise calculations
        for i in range(dim):
            for j in range(dim):
                #Don't compare alternative to itself
                if i is not j:
                    #calculate sum(Na, Nb) where Na = weightA*(stdM-stdN) 
                    #and Nb = weightB*(stdO-stdP) for each crit pair of A and B
                    Ni_vals = []
                    for k in quant_cols:
                        print "i:"+str(i)+"j:"+str(j)+"k:"+str(k)
                        crit_weight_A = float(crit_weights[k])
                        print "crit weight A: "+str(crit_weight_A)
                        std_val_A = float(in_matrix[i][k])
                        print "std_val_A: "+str(std_val_A)
                        std_val_B = float(in_matrix[j][k])
                        print "std_val_B: "+str(std_val_B)
                        Ni = crit_weight_A * (std_val_A - std_val_B)
                        print "Ni: "+str(Ni)
                        Ni_vals.append(Ni)
                    mat[i][j] = sum(Ni_vals)
        return mat
    
    def initialize_array(self, rows, cols):
        mat = []
        for x in range(rows):
            mat.append([0.0] * cols)
        return mat
    
    def absolute(self, matrix):
        new_matrix = deepcopy(matrix)
        for row in new_matrix:
            for val in row:
                val = abs(val)
        return new_matrix

if __name__ == "__main__":
    #India 1 input, rows-criteria, rols-alternatives
    input = [
        [4,3,4,2,4,3,3,2,2,2,3,4,2,1,1,3,2,3,37900,0],
        [3,2,3,3,4,2,3,2,2,2,3,4,3,2,1,3,3,3,3000,15000],
        [3,3,3,4,4,4,3,4,2,2,2,4,4,1,1,3,2,3,240,256],
        [4,4,3,4,3,4,3,4,2,2,2,4,4,1,1,3,2,3,12231,5000],
        [2,2,3,4,4,4,3,4,2,2,2,4,4,1,1,3,3,1,25,700],
        [3,3,3,2,2,3,1,2,2,3,3,4,2,1,1,3,3,3,19700,15700],
        [3,3,2,2,2,3,2,2,2,2,2,4,3,1,1,3,2,3,119648,300],
        [3,2,3,2,2,3,1,2,2,3,3,4,3,1,1,3,3,3,14875,15700]
    ]
    #India 1 data, matches evamix spreadsheet, old delphos uses same data in different order
    crit_weights = [1,1,2,1,1,1,4,2,2,1,2,2,1,1,3,3,4,3,3,1]
    crit_types = ["Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Ordinal","Binary","Ordinal","Ordinal","Ordinal","Ordinal","Ratio","Ratio"]
     
    print "Input:"
    for i in range(len(input)):
        print input[i]
    print ""
    print "Weightings:"
    print crit_weights

    #Do analysis
    evamix_tool = Evamix()
    try:
        evamix_tool.do_analysis(input, crit_weights, crit_types)
    except DelphosError, e:
        print "Error: "+str(e)

def load_input_from_csv(filename):
    reader = csv.reader(open(filename, "rbU"), "TSV")
    values = []
    
    for row in reader:
            values.append(row)
        
    for i in range(len(values)):
        for j in range(len(values[i])):
            #Convert cell value from string to integer
            values[i][j] = int(values[i][j])

    return values
import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from mca_wizard_ui import Ui_McaWizard
from util.common_functions import *
from util.latin_csv import *

class McaWizard(QDialog, Ui_McaWizard):
    """Manages the collection of MCA analysis input
    """
    def __init__(self, gui_manager, parent, project):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.project = project
        self.gui_manager = gui_manager
        self.isError = False    #Error flag for form processing
        self.errorMsg = ""
        self.default_template_extension = "csv"
        self.output_encoding = 'latin-1'
        self.cur_index = 0
        
        self.input_weights = None
        
        #Contains field data for all alternatives selected, each row is a 
        #list of [altern_id, altern_name]
        self.selected_altern_data = []
        self.selected_altern_ids = []
        self.selected_altern_names = []
        self.num_selected_alternatives = 0
        self.altern_id_column = 0 # in altern_data type list
        self.altern_name_column = 1    #in altern_data type list
        
        #Contains field data for all criteria selected, each row is a
        #list of [crit_id, crit_name, crit_type, crit_options, crit_cost_benefit]
        self.selected_crit_data = []
        self.selected_crit_ids = []
        self.selected_crit_names = []
        self.num_selected_criteria = 0
        self.crit_id_column = 0
        self.crit_name_column = 1
        self.crit_type_column = 2
        self.crit_options_column = 3
        
        #Button Signals
        QObject.connect(self.altern_next_button,QtCore.SIGNAL("clicked()"), self.process_altern_select)
        QObject.connect(self.crit_next_button,QtCore.SIGNAL("clicked()"), self.process_crit_select)
        QObject.connect(self.input_next_button,QtCore.SIGNAL("clicked()"), self.process_data_input)
        QObject.connect(self.weight_next_button,QtCore.SIGNAL("clicked()"), self.weight_next_click)
        
        QObject.connect(self.crit_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
        QObject.connect(self.input_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
        QObject.connect(self.run_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
        QObject.connect(self.weight_prev_button,QtCore.SIGNAL("clicked()"), self.weight_prev_click)
                    
        QObject.connect(self.altern_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.crit_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.input_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.weight_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.run_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)

        QObject.connect(self.check_all_altern_button,QtCore.SIGNAL("clicked()"), self.check_all_alternatives)
        QObject.connect(self.check_all_criteria_button,QtCore.SIGNAL("clicked()"), self.check_all_criteria)
        QObject.connect(self.uncheck_all_altern_button,QtCore.SIGNAL("clicked()"), self.uncheck_all_alternatives)
        QObject.connect(self.uncheck_all_criteria_button,QtCore.SIGNAL("clicked()"), self.uncheck_all_criteria)
        QObject.connect(self.equal_weight_button,QtCore.SIGNAL("clicked()"), self.assign_equal_weight)        
        QObject.connect(self.export_button,QtCore.SIGNAL("clicked()"), self.process_template_export)
        QObject.connect(self.import_button,QtCore.SIGNAL("clicked()"), self.process_template_import)        
        QObject.connect(self.run_analysis_button,QtCore.SIGNAL("clicked()"), self.process_run)
        
        #Other signals
        QObject.connect(self.mca_stack,QtCore.SIGNAL("currentChanged(int)"), self.process_current_change)
        
        self.setup_crit_select()        
        self.setup_altern_select()

    #################################### Alternatives #####################

    def setup_altern_select(self):
        self.altern_data = self.project.get_all_alternatives()
        self.altern_table.load(self.altern_data)    
        
    def process_altern_select(self):
        selected_altern_indexes = self.altern_table.get_selected_indexes()
        self.selected_altern_data = []
        self.selected_altern_ids = []
        self.selected_altern_names = []
        
        if len(selected_altern_indexes) < 2:
            QMessageBox.critical(self,"Error", "You must select at least two alternatives")
        else:
            for index in selected_altern_indexes:
                self.selected_altern_data.append(self.altern_data[index])
                self.selected_altern_ids.append(self.altern_data[index][self.altern_id_column])
                self.selected_altern_names.append(self.altern_data[index][self.altern_name_column])
            self.next_click()
        self.num_selected_alternatives = len(self.selected_altern_data)
        
    def check_all_alternatives(self):
        self.altern_table.check_all()
    
    def uncheck_all_alternatives(self):
        self.altern_table.uncheck_all()
    
    ################################ Criteria #################################

    def setup_crit_select(self):
        self.crit_data = self.project.get_all_criteria()
        self.crit_table.load(self.crit_data)

    def process_crit_select(self):
        selected_crit_indexes = self.crit_table.get_selected_indexes()
        if len(selected_crit_indexes) < 1:
            QMessageBox.critical(self,"Error", "You must select at least one criteria")
        else:
            #Build list of selected crit data
            self.selected_crit_data = []
            self.selected_crit_ids = []
            self.selected_crit_names = []
            self.selected_crit_types = []
            for index in selected_crit_indexes:
                crit = self.crit_data[index]
                self.selected_crit_data.append(crit)
                self.selected_crit_ids.append(crit[self.crit_id_column])
                self.selected_crit_names.append(crit[self.crit_name_column])
                self.selected_crit_types.append(crit[self.crit_type_column])
            self.next_click()
        self.num_selected_criteria = len(self.selected_crit_data)

    def check_all_criteria(self):
        self.crit_table.check_all()

    def uncheck_all_criteria(self):
        self.crit_table.uncheck_all()
               
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
            if cur_type == "Ratio":
                quant_list.append(i)
            elif cur_type == "Ordinal" or cur_type == "Binary":
                qual_list.append(i)
        return (quant_list, qual_list)

    ################################# Input Data ##############################

    def setup_data_input(self):
        self.input_table.load(self.selected_altern_data, self.selected_crit_data)

    def process_template_export(self):
        """Creates a unicode CSV containing alternatives and criteria for quickly inputting data
        """
        fd = QtGui.QFileDialog(self)
        fd.setFileMode(QFileDialog.AnyFile)
        template_filename = fd.getSaveFileName()
        #Check if filename and if extension already added
        if template_filename:
            if not re.search('[.]'+self.default_template_extension+'$', template_filename):
                template_filename += '.'+self.default_template_extension

            export_arr = initialize_str_array(self.num_selected_criteria+1, self.num_selected_alternatives+2)
            #add alternatives to first row leaving first two cells blank
            export_arr[0] = ["",""]+self.selected_altern_names            
            #add criteria data to first two columns leaving top left cell blank
            for i in range(self.num_selected_criteria):
                (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = self.selected_crit_data[i]
                
                #Add criteria name to first column
                export_arr[i+1][0] = crit_name
                
                #Build option/unit string and add to second column
                crit_option_str = ""                
                if crit_type == "Ordinal" or crit_type == "Binary":
                    for option in crit_options_units:
                        (name, value) = option
                        crit_option_str += "("+unicode(value)+" = "+unicode(name)+")"
                elif crit_type == "Ratio":
                    crit_option_str += "(# "+unicode(crit_options_units)+")"
                    
                export_arr[i+1][1] = crit_option_str

            #Add comments to file explaining the structure
            comments =     [
                            [""],
                            [""],
                            [""],                                                                                  
                            ["*******************************************************************"],
                            ["* This file was generated by Delphos and should ONLY\n   be used to enter data."],
                            ["*"],
                            ["****** File structure ******"],
                            ["*"],
                            ["* Row 1: alternative names (starting with column C)"],
                            ["* Column A: criteria names"],
                            ["* Column B: criteria values with text description"],
                            ["*"],
                            ["****** Instructions ******"],
                            ["*"],
                            ["* - If using a spreadsheet program, resize the"],
                            ["    columns so you can see everything"],
                            ["* - The alternatives and criteria form a"],
                            ["    pair-wise matrix."],
                            ["* - Enter a value for each pair, starting in"],
                            ["    row 2, column C."],
                            ["* - For Ordinal and Binary criteria, enter an"],
                            ["    integer value from the list of possible"],
                            ["    options in column B."],
                            ["* - For Ratio criteria, enter a positive integer"],
                            ["    value, the units for that value are given"],
                            ["    in column B."],
                            ["* - DO NOT add extra criteria or alternatives"],
                            ["    they will not be read."],
                            ["* - DO NOT remove any alternatives or criteria"],                      
                            ["* - DO NOT re-arrange rows/columns as they are"],
                            ["    expected in the order they were exported."],
                            ["* - After inputting data, be sure to resave as"],
                            ["    as a CSV file"],
                            ["* - On Apple Macs you may need to save the file in"],
                            ["   'CSV (Windows)' format"],
                            [""],
                            ["* Failure to follow directions may produce unexpected results!"],
                            ["*******************************************************************"],                            
                        ]
                                
            #output list to CSV.  Use latin1 encoding
            writer = csv.writer(open(template_filename, "wb"), csv.excel)
            writer.writerows(export_arr)
            writer.writerows(comments)
            
            QMessageBox.critical(self,"Template Exported", "CSV Template successfully exported to "+template_filename+"\n\nPopulate this template with data and import it back into Delphos")

    def process_template_import(self):
        """Reads in input from a template
        """
        fd = QtGui.QFileDialog(self)
        fd.setFileMode(QFileDialog.ExistingFile)
        fd.setFilter("*."+self.default_template_extension)
        template_filename = fd.getOpenFileName()

        if template_filename:
            if not re.search('[.]'+self.default_template_extension+'$', template_filename):
                QMessageBox.critical(self,"Error", "You did not select a CSV file (."+self.default_template_extension+" file extension)")
            else:
                f = open(template_filename, "r")
                reader = csv.reader(f, dialect=csv.excel)
                
                #Load part of input we care about into 2D list, the pair-wise matrix
                import_list = []
                for i in range(self.num_selected_criteria+1):
                    row = reader.next()
                    if i is not 0:
                        #append all but first two columns
                        import_list.append(row[2:])
            
                #i = imported value, e = expected value
                for i in range(self.num_selected_criteria):
                    for j in range(self.num_selected_alternatives):
                        #print "i: "+str(i)+"j: "+str(j)
                        i_crit_name = self.crit_data[i][self.crit_name_column]
                        #print "i_crit name: "+unicode(i_crit_name)
                        i_altern_name = self.selected_altern_data[j][self.altern_name_column]
                        #print "i_altern name: "+unicode(i_altern_name)
                        i_value = import_list[i][j]
                        #print  "i_value: "+unicode(i_value)
                
                success = self.input_table.load(self.selected_altern_data, self.selected_crit_data, import_list)
                if success:
                    QMessageBox.information(self,"Success", "CSV loaded successfully")
                else :
                    QMessageBox.critical(self,"Error", "Due to error, table may only be partially loaded")
        
    def process_data_input(self):
        #Get data from table
        self.input_data = self.input_table.get_input_data(self.selected_altern_names, self.selected_crit_names)
        
        #Get lists describing which columns (criteria) in in_matrix are quantitative and which are qualitative
        (quant_cols, qual_cols) = self.gen_crit_type_lists(self.selected_crit_types)
        num_qual_criteria = len(qual_cols)
        num_quant_criteria = len(quant_cols)
        
        if self.input_data:
                success = self.input_data_checks(num_quant_criteria, num_qual_criteria, quant_cols, qual_cols)
                if success:
                    #for row in self.input_data
                    #    print row
                    self.next_click()

    def input_data_checks(self, num_quant_criteria, num_qual_criteria, quant_cols, qual_cols):
        #Check if for any quant criteria, the values are the same for all alternatives
        if num_quant_criteria > 0:
            for j in quant_cols:
                first_val = self.input_data[0][j]
                same = True
                for i in range(len(self.input_data)):
                    if self.input_data[i][j] != first_val:
                        same = False
                if same:
                    QMessageBox.critical(self,"Input Error", "Your quantitative values for '"+self.selected_crit_names[j]+"' (row "+str(j+1)+ ") are all the same.  At least one cell in this row must have a value different from the rest.")
                    return False

        #Check if for any qualitative criteria, the values are the same for all alternatives
        if num_qual_criteria > 0:
            same = True
            for j in qual_cols:
                first_val = self.input_data[0][j]
                for i in range(len(self.input_data)):
                    if self.input_data[i][j] != first_val:
                        same = False
            if same:
                QMessageBox.critical(self,"Input Error", "Your rows with ordinal/binary criteria all have the same value.  At least one of those rows must have a cell with a value different from the rest.")
                return False
        return True

    ########################## Input Weights #########################

    def weight_next_click(self):
        ok = self.process_weight_input("forward")
        if ok:
            self.next_click()

    def weight_prev_click(self):
        ok = self.process_weight_input("backward")
        if ok:
            self.prev_click()

    def setup_weight_input(self):
        if not self.input_weights:
            self.input_weights = InputWeightSet(self.selected_crit_data)
        else:
            self.input_weights.update_crits(self.selected_crit_data)
        self.weight_table.load(self.input_weights)

    def process_weight_input(self, direction):
        input_required = True
        if direction == "backward":
            input_required = False
            
        new_input_weights = self.weight_table.get_input_weights(input_required)
        self.input_weights.update_weights(new_input_weights)            
        if self.input_weights:
            return True
        else:
            return False

    def assign_equal_weight(self):
        self.weight_table.assign_equal_weight()

    ############################### Run #################################
    
    def setup_run(self):
        self.num_alternatives_label.setText(str(self.num_selected_alternatives))
        self.num_criteria_label.setText(str(self.num_selected_criteria))

    def process_run(self):
            """Processes clicking of 'Run Analysis' button
            """
            if self.isError:
                self.isError = False
            else:
                self.emit(SIGNAL("mca_analysis_info_collected"), self.selected_altern_data, self.selected_crit_data, self.input_data, self.input_weights.get_weights(), self.selected_crit_types)

    ############################# General ###############################

    def next_click(self):
        """Shift stack forward one
        """
        current_index = self.mca_stack.currentIndex()
        self.mca_stack.setCurrentIndex(current_index+1)

    def prev_click(self):
        """Shift stack back one
        """
        current_index = self.mca_stack.currentIndex()
        prev_widget = self.mca_stack.widget(current_index-1)
        self.mca_stack.setCurrentWidget(prev_widget)    

    def process_reject(self):
        """Processes clicking of Cancel button in dialog
        """
        self.hide()
        self.deleteLater()
    
    def process_current_change(self, index):
        """Loads the appropriate widget when the next button is clicked
        """
        ok = False
        if self.cur_index < index:
            if index is 2:
                self.setup_data_input()
            elif index is 3:
                self.setup_weight_input()
            elif index is 4:
                self.setup_run()
                
        self.cur_index = index
       
class InputWeightSet():
    """Maintains weights input by the user.
    
    Ties weight values input by user to their associated criterion so
    that the user can go back and change the criteria without losing
    the data that they already input.  It also separates data from 
    presentation.
    """
    def __init__(self, crit_data):
        #TODO: Really we should only be keeping the id, name and weight
        self.crit_id_column = 0
        self.crit_name_column = 1
        self.weight_column = 2        

        self.weight_data = self.create_weight_data(crit_data)

        print "Creating weight set"
        print self.weight_data

    def create_weight_data(self, crit_data):
        """Given a critieria set, create an empty weight set
        """
        weight_data = []
        for crit in crit_data:
            id = crit[self.crit_id_column]
            name = crit[self.crit_name_column]
            weight_data.append([id, name, None])
        return weight_data
            
    def update_weights(self, new_weights):
        
        if not new_weights or len(new_weights) != len(self.weight_data):
            raise Exception, "Error updating weights"

        print "Weights before: "
        print self.get_weight_data()

        print "New weights: "
        print new_weights

        for i in range(len(new_weights)):
            self.weight_data[i][self.weight_column] = new_weights[i]
                  
        print "Update weights"
        print self.get_weight_data()

    def update_crits(self, new_crit_data):
        print "New crit data"
        print new_crit_data
    
        #Create new weight data
        new_weight_data = self.create_weight_data(new_crit_data)
        #Transfer weight values
        for i in range(len(self.weight_data)):    
            for j in range(len(new_weight_data)):
                if new_weight_data[j][self.crit_id_column] == self.weight_data[i][self.crit_id_column]:
                    new_weight_data[j][self.weight_column] = self.weight_data[i][self.weight_column]                
        
        #Drop the old weight data
        self.weight_data = new_weight_data
        
        print "Updated crit data"
        print self.weight_data
    
    def get_weight_data(self):
        return self.weight_data
    
    def get_weights(self):
        weights = []
        for item in self.weight_data:
            weights.append(item[self.weight_column])
        return weights
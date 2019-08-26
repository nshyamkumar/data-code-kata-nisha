#################################################################################################
#===========================================================================#####################
#Implements tests as part of TDD to check the functionality of the code in FWFtoCSVConverter.py##
#Makes use of Python's 'unittest' module                                                 ########
######## Creating test cases is accomplished by subclassing 'unittest.TestCase'     #############
#========================  Author- Nisha Shyamkumar ===================         #################
#===========================================================================#####################
#################################################################################################

#################################################################
#######################Import Packages###########################
#################################################################

import unittest
import csv
from FWFtoCSVConverter import *

########################################################################################################
#######################Class to implement testcases#####################################################
#Each method in this class is a test for the corresponding function in FWFtoCSVConverter.py#############
##Testmethods are named to refect the name of the function being tested#################################                                                        ############
########################################################################################################
class testFWFtoCSVConverter(unittest.TestCase):
    
###################################################################################################################
#####Tests the functionality of readSpec() function in FWFtoCSVConverter.py########################################
###Defined the expected output ( a dictionary with expected values )###############################################
###Verifies if readSpec function reads the config file and the result matches with expected output ################
#self.assertEqual()compares the function call output with expected output and throws error if both don't match#####
###################################################################################################################
    def test_readSpec(self):
        dict_test_op = {'ColumnNames': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'], 
        'Offsets': ['5', '12', '3', '2', '13', '7', '10', '13', '20', '13'], 
        'FixedWidthEncoding': 'windows-1252', 
        'IncludeHeader': 'True', 'DelimitedEncoding': 'utf-8'}
        self.assertEqual(readSpec(CONFIGFILE), dict_test_op)
###################################################################################################################
#####Tests the functionality of buildHeaderForFWF() function in FWFtoCSVConverter.py###############################
###Defined a sample expected output ( a list with expected values)      ###########################################
###Verifies if buildHeaderForFWF() takes the sample inputs  and the result matches with expected output############
#self.assertEqual()compares the function call output with expected output and throws error if both don't match#####
###################################################################################################################    
    def test_buildHeaderForFWF(self):
        dict_test_ip = {'ColumnNames': ['C1', 'C2'], 
        'Offsets': ['3', '4'] }
        test_op = 'C1 C2  '
        self.assertEqual(buildHeaderForFWF(dict_test_ip),test_op)
###################################################################################################################
#####Tests the functionality of buildFwfRec() function in FWFtoCSVConverter.py#####################################
###Defined a sample expected output ( a list with expected values)      ###########################################
###Verifies if buildFwfRec() takes the sample inputs  and the result matches with expected outp####################
#self.assertEqual()compares the function call output with expected output and throws error if both don't match#####
###################################################################################################################         
    def test_buildFwfRec(self): 
        dict_test_ip = {'ColumnNames': ['C1', 'C2'], 
        'Offsets': ['3', '4'] }
        linelist_test_ip = ['OurM','MayMail']
        test_op = ['OurM   ', 'MayMail']
        self.assertEqual(buildFwfRec(dict_test_ip, linelist_test_ip),test_op) 
####################################################################################################################
#####Tests the functionality of writeFwfFile() function in FWFtoCSVConverter.py#####################################
###The test method reads the actual outputfile(fwffile) and checks if it generated the expected number of records ##
##self.assertEqual()compares the function call output with expected output and throws error if both don't match#####
####################################################################################################################     
    def test_writeFwfFile(self):
        with open(FWFFILE,'r') as ffwf:
            line_count = 0
            f_content = ffwf.readlines()
            for row in f_content:
                line_count+=1
            ffwf.close()
        self.assertEqual(line_count,3)
####################################################################################################################
#####Tests the functionality of convertOffsetsToInt() function in FWFtoCSVConverter.py##############################
###Verifies if convertOffsetsToInt() takes the sample inputs(list of numbers stored as strings) #################### 
######and the result matches with expected output which is a list of those numbers as inegers#######################                                                                ##
##self.assertEqual()compares the function call output with expected output and throws error if both don't match#####
####################################################################################################################         
    def test_convertOffsetsToInt(self):
        list_test = ['4','5','6']
        self.assertEqual(convertOffsetsToInt(list_test),[4,5,6])
####################################################################################################################
#####Tests the functionality of cfwfToCSVWriter() function in FWFtoCSVConverter.py    ##############################
###The test method reads the actual outputfile(fwffile) and checks if it generated the expected number of records### 
######The test covers format of the file as csv and delimiter as pipe character              #######################                                                                ##
##self.assertEqual()compares the function call output with expected output and throws error if both don't match#####
####################################################################################################################     
    def test_fwfToCSVWriter(self):
        with open(OPCSVFILE,'r') as fcsv:
            csv_reader = csv.reader(fcsv, delimiter='|')
            line_count = 0
            for row in csv_reader:
                line_count+=1
            fcsv.close()
        self.assertEqual(line_count,3)
        
#########################################################################################
######################### Main function                  ################################
###### Call to each test is added only when call to previous ############################
#### method and its execution was succesful and returned the expected output.  ##########
#########################################################################################

if __name__ == '__main__':
    test = testFWFtoCSVConverter()
    test.test_readSpec()
    test.test_buildHeaderForFWF()
    test.test_buildFwfRec()
    test.test_writeFwfFile()
    test.test_convertOffsetsToInt()   
    test.test_fwfToCSVWriter()
    print('****Succesfully completed testing of FWFtoCSVConverter.py******************\n')

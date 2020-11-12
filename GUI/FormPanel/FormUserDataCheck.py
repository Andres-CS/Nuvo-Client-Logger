#Checks data entered by the user is the correct.

import wx

''' Check if there is any user field missing, if so return TRUE otherwise FALSE '''
def form_missingdata(section0, section1_1, section1, section2, section3, section4):
    missing = False

    #Client Choice Menu with index 1
    if(section0[1].GetSelection() == -1):
        missing = True

    #----- Redio Box (Button) DATA -------
    if(section1_1[0].GetSelection() == " NOT_FOUND"):
        missing = True

    #Test All Text fields are Entered
    for item in section1:
        #TextCtrl is item with index 1
        #Empty String
        if not item[1].GetLineText(0):
            missing = True

    #----- Radio Button DATA -------
    if(section2[1].GetValue() == False | section2[2].GetValue() == False):
        missing = True

    #----- Paper Type DATA -------
    #Paper Choice menu with index 2
    if(section3[2].GetSelection() == -1):
        missing = True
    
    #----- Binding & Inserts -------
    #BINDING
    if(section4[1][1].GetSelection() == -1):
        missing = True
    #INSERTS
    if(section4[2][1].GetValue() == -1):
        missing = True

    return missing


''' form_correctDataType, converts any necesary value that needs to be an integer into and intger; '''
def form_correctDataType(INPUTDATA):
    #Fields that need to be integer;
    int_field = ["Job ID","Number of Copies","Number of Pages","Siding","Number of Printers"]
    for field in int_field:
        if(INPUTDATA[field]):
            #Make field an integer
            INPUTDATA[field]=int(INPUTDATA[field])
    #Return Dictionary
    return INPUTDATA

'''
    Check that data entered by user in the text control fields are the appropiate
    data type.

    This should concur with the data type on which the Databased of the application
    is based.
    The following is based on the GuiSetUp.py file.

    "fields_name" = ["Job ID","Job Name","Number of Copies","Number of Pages","Siding","TypePaper", "TypePrinter","Type of Book","NumSheets","NumCartons","Coil","Number of Printers","TimePrinting"]
    "fields_type" : ["INTEGER PRIMARY KEY","TEXT","INTEGER","INTEGER","TEXT","TEXT", "TEXT","TEXT","INTEGER","INTEGER","REAL","INTEGER","TEXT"]
'''

def form_checkDatatype(INPUTDATA):
    correctData = True
    #Get dict keys
    IpDt_keys = list(INPUTDATA.keys())

    #Database Fields. For reference
    fields_name = ["Job ID","Job Name","Number of Copies","Number of Pages","Siding","TypePaper", "TypePrinter","Type of Book","NumSheets","NumCartons","Coil","Number of Printers","TimePrinting"]
    fields_type = ["INTEGER PRIMARY KEY","TEXT","INTEGER","INTEGER","INTEGER","TEXT", "TEXT","TEXT","INTEGER","INTEGER","REAL","INTEGER","TEXT"]

    #Traverse the keys in INPUTDATA
    for k in IpDt_keys:
        #Find if Key in fields_name
        if k in fields_name:
            #Get Index of fields_name's fields_type
            index = fields_name.index(k)
            #Classife the type of datatype
            if "TEXT" in fields_type[index]:
                correctData = isinstance(INPUTDATA[k], str)
            if "INTEGER" in fields_type[index]:
                correctData = isinstance(INPUTDATA[k], int)
    return correctData

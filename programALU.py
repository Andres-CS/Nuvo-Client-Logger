#This Functions here take care of calculating the results based on the user data.

import json
import time
from Profiles.paperPfl import paperPfl
from Profiles.bindingPfl import SprBnd


def get_sizeof_coil(nsheets, coilprofile):
    #Type of coil to use
    size_to_use = list()

    #Get all coil sizes and make INT
    coil_sizes = list(SprBnd().get_binding_profileAttr(coilprofile))

    for x in range(len(coil_sizes)):
        coil_sizes[x] = int(coil_sizes[x])

    #Sort coil size
    coil_sizes.sort()

    #Determine size of coil
    for i in range(len(coil_sizes)):
        if coil_sizes[i] == int(nsheets):
            size_to_use = SprBnd().get_binding_profileAttr(coilprofile)[str(coil_sizes[i+1])]
            break
        elif coil_sizes[i] > int(nsheets):
            size_to_use = SprBnd().get_binding_profileAttr(coilprofile)[str(coil_sizes[i])]
            break
    
    #Convert to Fraction
    size_to_use[0] = str(size_to_use[0]*16)+"/16"

    #Makes List in to String
    size_to_use = str(size_to_use[0])+" "+str(size_to_use[1])

    return size_to_use


def ALU(userData):
    #Results holder
    results = dict()

    #Fields name for reference. Based on the DataBase
    fields_name = ["Number of Copies","Number of Pages","Siding","TypePaper", "TypePrinter","NumSheets","NumCartons","Coil","Number of Printers","Time Printing"]

    #Get Paper Specifications
    paper_profile_spcs = paperPfl().get_profileAttr(userData["Paper"])

    '''---Perform Paper Calculations---'''
    #Total Number of Sheets
    NumSheets = (userData["Number of Pages"] * userData["Number of Copies"] ) / userData["Siding"]
    #Number of Sheet per Book
    NumSheet_PerBook = NumSheets / userData["Number of Copies"]
    #Number of Rims
    NumRims = NumSheets / paper_profile_spcs["sheet_per_rim"]
    #Number of Cartons
    NumCartons = NumRims / paper_profile_spcs["rim_per_carton"]

    #Populate Results Dict
    results["Number Sheets"] = NumSheets
    results["Number Sheet Per Book"] = NumSheet_PerBook
    results["Number Rims"] = NumRims
    results["Number Cartons"] = NumCartons

    '''---Perform Spiral Binding Calculations---'''
    #Get Type of Spiral Biding
    #If user selected None as the profile then 
    if(userData["Coil"] == "None"):
        results["Coil Size"] = userData["Coil"]
    else:
        #Otherwise.....
        results["Coil Size"] = get_sizeof_coil(NumSheet_PerBook,userData["Coil"])

    results["Time Printing"] = time.asctime()
    return results

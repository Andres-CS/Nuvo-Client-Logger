import json
import os

# Set Up File -> Reads all the files needed to setup the GUI part of the application.
from Profiles.paperPfl import paperPfl
from Client.ClientMgt import get_clients



additionalData = {
    "Clients":get_clients(),
    "Papers": paperPfl().get_profilesnames(),
    "Printers": ["TOSHIBA","CANON"],
    "Bindings": ["None","Wire","Plastic Coil","Plastic Combo"],
}

#---------------------- GUI CONFIG RETRIVAL ------------------------

def FormSections(gui_config,section,rows=0):
    section_widgets = []
    section = str(section)
    #Parse Widgets Section
    for r in range(rows):
        row = str(r)
        for widget in gui_config[section][row]:
            for properties in gui_config[section][row][widget]:
                #If its a Menu
                if gui_config[section][row][widget][properties] == "Menu":
                    #Do we need to call an external function to get Menu Items?
                    if gui_config[section][row][widget]["callFunction"] == True:
                        #Get Profiles Meta-Data
                        section_widgets.append(
                            additionalData[
                                gui_config[section][row][widget]["functionName"]
                                ]
                            )
                        break
                if widget in section_widgets:
                    continue
                else:
                    section_widgets.append(widget)
    return section_widgets


'''
get_label_settings:
    *is a functions that accepts n number of parameters.
    *Each aparamter could be a list(of string), or string be itself.
    *These parameter are stored in a list and then return as a list.
    *They are the text to be used on the widgets in the application.
'''
def get_lable_settings(*listofprofiles):
    profiles   = list()

    #loop through list of profiles
    for prfl in listofprofiles:
        profiles.append(prfl)

    return profiles

def get_label_settings(listofprofiles):
    profiles   = list()

    #loop through list of profiles
    for prfl in listofprofiles:
        profiles.append(prfl)

    return profiles

#---------------------- FORM PANEL ------------------------

see_profile = "See Profile"

#Get Widgets Set
spec_file_GUI = os.path.join(os.path.dirname(__file__),"_CONFIG/FormPanel_WidgetsSetup.json")

with open(spec_file_GUI) as config:
    gui_File = json.load(config)


F_sec_0 = get_label_settings( FormSections(gui_File,1,1) )
F_sec_1 = get_label_settings( FormSections(gui_File,2,6) )
F_sec_2 = get_label_settings( FormSections(gui_File,3,2) )
F_sec_3 = get_label_settings( FormSections(gui_File,4,3) )
F_sec_4 = get_label_settings( FormSections(gui_File,5,3) )
F_sec_5 = get_label_settings( FormSections(gui_File,6,1) )

Labels_for_UserForm = [F_sec_0,F_sec_1,F_sec_2,F_sec_3,F_sec_4,F_sec_5]

# ----------------------- RECORD PANEL ----------------------

R_sec_0 = get_lable_settings("Search by: ")
R_sec_1 = get_lable_settings(["Client","Job #","Date "],["Search"])
R_sec_2 = get_lable_settings("Data")
R_sec_3 = get_lable_settings("Clear Search")

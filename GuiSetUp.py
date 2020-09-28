# Set Up File -> Reads all the files needed to setup the GUI part of the application.
from Profiles.paperPfl import paperPfl
from Client.ClientMgt import get_clients
import json

#---------------------- GUI RETRIVAL ------------------------

def sec1(gui_config):
    section_widgets = []
    #Parse Widgets Section 
    for widget in gui_config["1"]["1"]:
        for properties in gui_config["1"]["1"][widget]:
            if gui_config["1"]["1"][widget][properties] == "Menu":
                if gui_config["1"]["1"][widget]["callFunction"] == True:
                    #Get Clients
                    section_widgets.append(get_clients())
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



def tt_(listofprofiles):
    profiles   = list()

    #loop through list of profiles
    for prfl in listofprofiles:
        profiles.append(prfl)

    return profiles

#---------------------- FORM PANEL ------------------------

see_profile = "See Profile"

#Get Widgets Set
with open("./widgetsSetup.json") as config:
    gui_File = json.load(config)


F_sec_0 = tt_(sec1(gui_File))
#F_sec_0=get_lable_settings("Client   ", get_clients(), "New Client")

F_sec_1=get_lable_settings("Job ID","Job Name","Type of Book","Number of Copies","Number of Pages","Number of Printers")
#F_sec_1=get_lable_settings("Job ID","Job Name","Type of Book","Number of Copies","Number of Pages","Number of Printers")

F_sec_2=get_lable_settings("Type of Siding","Single","Double")
F_sec_3= get_lable_settings("PROFILES SELECTION", "Paper", paperPfl().get_profilesnames(), see_profile, "Printer", ["TOSHIBA","CANON"],see_profile )
F_sec_4 = get_lable_settings("Extras","Binding",["None","Wire","Plastic Coil","Plastic Combo"], "Inserts")
F_sec_5 = get_lable_settings("Submitt")

Labels_for_UserForm = [F_sec_0,F_sec_1,F_sec_2,F_sec_3,F_sec_4,F_sec_5]

# ----------------------- RECORD PANEL ----------------------

R_sec_0 = get_lable_settings("Search by: ")
R_sec_1 = get_lable_settings(["Client","Job #","Date "],["Search"])
R_sec_2 = get_lable_settings("Data")
R_sec_3 = get_lable_settings("Clear Search")

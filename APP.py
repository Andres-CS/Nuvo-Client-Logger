import wx

'''Databse Setup'''
from Database.Database_Setup import DB_Setup #LEGACY
from AppSetup import setUp

'''GuiSetUp: reads config files for the panels'''
from GUI.GuiSetUp import Labels_for_UserForm
from GUI.GuiSetUp import R_sec_0, R_sec_1, R_sec_2, R_sec_3

'''ApplicationClc, MainFrameGui: modules used for creation of skeleton for window app.'''
from GUI.Application import JobRegister
from GUI.MainFrameGui import mainFrame

'''SideNavegation: moduel used to create left-align tab menu for panel navegation.'''
from GUI.SideNavegation import tabPanel, TabMenu

'''FormPanelGui, RecordPanelGui: modules used to create the appropiate GUI sections of the window app.'''
from GUI.FormPanel.FormPanelGui import formPanel
from GUI.RecordsPanel.RecordPanelGui import recordPanel



#-------------------MAIN ----------------------

def main():
    #Database Setup
    #DB_Setup()
    setUp()

    #Create Application Obj
    application = JobRegister()

    #Create Window Frame
    Main_Window_frame = mainFrame(None)

    #Create Side Tabs
    Main_Panel = tabPanel(Main_Window_frame)
    Left_Menu_Tabs = TabMenu(Main_Panel)

    #Create Form Panel
    Form_panel = formPanel(Left_Menu_Tabs, Labels_for_UserForm)

    #Create Record Panel
    #Record_panel = recordPanel(Left_Menu_Tabs, R_sec_0, R_sec_1, R_sec_2, R_sec_3)

    #Add Tabs to Tab Menu(in other words, the panels)
    Left_Menu_Tabs.AddPage(Form_panel,"Form")
    #Left_Menu_Tabs.AddPage(Record_panel,"Records")

    #Sizer for Tabs
    TabSizer = wx.BoxSizer()
    TabSizer.Add(Left_Menu_Tabs,1,wx.EXPAND)
    Main_Panel.SetSizer(TabSizer)


    #Display, or run, window Frame
    Main_Window_frame.Show()

    #Run Application
    application.MainLoop()
#-------------------------------------------------
main()

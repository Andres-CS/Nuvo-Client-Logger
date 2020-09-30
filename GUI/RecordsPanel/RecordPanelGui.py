#Log Panel

import wx
import wx.adv
import wx.lib.scrolledpanel as scrolled
import json
import os

from Client.ClientMgt import get_clients
from App_DB_Bridge import database


''' ---------- AXUILIARY METHODS ---------- '''

def set_search_parameters(objs):
    shell = {
        "client":objs[0],
        "jobid":objs[1],
        "timeprinting":objs[2]
    }
    return shell

''' ---------- RECORD PANEL CLASS - GUI ---------- '''

class recordPanel(scrolled.ScrolledPanel):
    def __init__(self,parent,Sec_0, Sec_1, Sec_2, Sec_3):
        scrolled.ScrolledPanel.__init__(self,parent,wx.ID_ANY)

        #Database 
        self.Search_Parameter = ["","",""]
        self.db_acc = database()

        #Widget Cretion
        self.wdgs_0 = self.sec_0_widgets(Sec_0)
        self.wdgs_1 = self.sec_1_widgets(Sec_1)
        self.wdgs_2 = self.sec_2_widgets(Sec_2)
        self.wdgs_3 = self.sec_3_widgets(Sec_3)

        #Sizer Definitino
        self.szr_0 = self.sizer_sec_0(self.wdgs_0)
        self.szr_1 = self.sizer_sec_1(self.wdgs_1)
        self.szr_2 = self.sizer_sec_2(self.wdgs_2)
        self.szr_3 = self.sizer_sec_3(self.wdgs_3)

        #Divider widget
        self.wdg_divider = list()
        for dvd in range(3):
            self.wdg_divider.append(wx.StaticLine(self,wx.ID_ANY,style=wx.HORIZONTAL))

        #Panel Sizer
        Rcd_Sizer = wx.BoxSizer(wx.VERTICAL)

        #Adding Sizer to Rcd_Sizer (Record Sizer)
        Rcd_Sizer.Add(self.szr_0,0,wx.ALL|wx.EXPAND,5)
        Rcd_Sizer.Add(self.wdg_divider[0],0,wx.ALL|wx.EXPAND,5)
        Rcd_Sizer.Add(self.szr_1,0,wx.ALL|wx.EXPAND,5)
        Rcd_Sizer.Add(self.wdg_divider[1],0,wx.ALL|wx.EXPAND,5)
        Rcd_Sizer.Add(self.szr_2,0,wx.ALL|wx.EXPAND,5)
        Rcd_Sizer.Add(self.wdg_divider[2],0,wx.ALL|wx.EXPAND,5)
        Rcd_Sizer.Add(self.szr_3,0,wx.ALL|wx.EXPAND,5)

        #Set Sizer
        self.SetSizer(Rcd_Sizer)

        self.SetupScrolling()

        #Binding Methods
        # --- Bind(event,handler,widget) | widget.Bind(event,handler) ---
        self.wdgs_1[0][0].Bind(wx.EVT_CHECKBOX , self.OnClick_CheckBox1) #1st CheckBox
        self.wdgs_1[0][2].Bind(wx.EVT_CHECKBOX , self.OnClick_CheckBox2) #2nd CheckBox
        self.wdgs_1[0][4].Bind(wx.EVT_CHECKBOX , self.OnClick_CheckBox3) #3th CheckBox
        self.wdgs_1[1][0].Bind( wx.EVT_BUTTON  , self.OnClickSearch) #Search Button Binding
        self.wdgs_3[0].Bind(wx.EVT_BUTTON, self.OnClickClearSearch) #Clear Button Search 

    '''---------------------------------------------------
                    SECTION METHODS
    ---------------------------------------------------'''

    def sec_0_widgets(self,labels):
        widgs = list()
        for lbs in labels:
            widgs.append(wx.StaticText(self,wx.ID_ANY,lbs))

        return widgs

    def sec_1_widgets(self,labels):
        '''
        Section 1 consists of two groups:
            group 1: is parameter search the client will select. e.i. Client,Job #,Date
            group 2: is just the submitt/search button

        They will be place in the same BoxSizer in a HORIZONTAL style, once the Sizer are created.
            *---------------------*
            |  Group 1 | Group 2  |
            *---------------------*

        '''
        widgs = list()
        #Group 1
        widgs.append(self.sec_1_wdg_group_1(labels[0]))
        #Group 2
        widgs.append(self.sec_1_wdg_group_2(labels[1]))

        return widgs

    def sec_1_wdg_group_1(self,labels):
        '''
        This group will consists of a Radio Button preceded by a Choice/Text field widget.

            *---------------------------------*
            |  Check Btn  | Choice/TextField  |
            *---------------------------------*
            |  Check Btn  | Choice/TextField  |
            *---------------------------------*

        The widgets will be store in an array with the first widget(index 0) as the upper left
        Radio Button  and the last widget (index n-1) as the lower rigth Choice/TextField.

        '''
        wdgs = list()

        wdgs.append(wx.CheckBox(self,wx.ID_ANY,labels[0]))
        wdgs.append(wx.Choice(self,wx.ID_ANY,choices=get_clients(), style=wx.CB_SORT))
        wdgs.append(wx.CheckBox(self,wx.ID_ANY,labels[1]))
        wdgs.append(wx.TextCtrl(self,-1,''))
        wdgs.append(wx.CheckBox(self,wx.ID_ANY,labels[2]))
        wdgs.append(wx.adv.DatePickerCtrl(self,wx.ID_ANY,style=wx.adv.DP_DROPDOWN))

        return wdgs

    def sec_1_wdg_group_2(self,labels):
        '''
        This Group consists of a single button (as of this date 8/14/2018) that will trigger the a quary to the database
        '''
        wdgs = list()

        for lbs in labels:
            wdgs.append(wx.Button(self,wx.ID_ANY,lbs))

        return wdgs

    def sec_2_widgets(self,labels):
        wdgs = list()
        lsctl =  wx.ListCtrl(self,wx.ID_ANY,style=wx.LC_REPORT|wx.BORDER_SUNKEN)

        #Access DB to get Data
        query_result = self.db_acc.get_data(set_search_parameters(self.Search_Parameter))

        
        #Add Colums - These columns are the columns that exist in the DB.
        columns = self.db_acc.get_ColHeading()
        for heading in columns:
            lsctl.AppendColumn(heading) #Columns should be the labes.

        #Add Rows - These are the data obtain from the DB.
        for rws in range(len(query_result)):
            lsctl.InsertItem(rws,"")
            for clm in range(len(query_result[rws])):
                lsctl.SetItem(rws,clm,str(query_result[rws][clm]))

        wdgs.append(lsctl)

        return wdgs

    def sec_3_widgets(self,labels):
        '''
        This section Contains, up to this date 8/15/2018, a button that cleare the query made to the database
        '''
        wdgs = list()
        for lbs in labels:
            wdgs.append(wx.Button(self,wx.ID_ANY,lbs))

        return wdgs

    '''---------------------------------------------------
                    SIZER METHODS
    ---------------------------------------------------'''

    def sizer_sec_0(self,widgs):
        '''
        Sizer for this section is a BoxSizer with VERTICAL style.
        This allows to insert more widgets if needed in a vertical
        manner.
        '''
        bxs = wx.BoxSizer(wx.VERTICAL)
        for wgs in widgs:
            bxs.Add(wgs,0,wx.ALL|wx.EXPAND,2)

        return bxs

    def sizer_sec_1(self,widgs):
        '''
        As mention above in the "sec_1_widgets" method this sectin is made of two groups.
        This groups will be placed in a HORIZONTAL style

        *---------------------*
        |  Group 1 | Group 2  |
        *---------------------*

         Each group will have a it layout explain in its sizer method creation.
        '''
        szr = wx.BoxSizer(wx.HORIZONTAL)
        #Group 1
        szr.Add(self.sizer_sec_1_grp_1(widgs[0]),0,wx.ALL|wx.EXPAND,0)
        #Group 2
        szr.Add(self.sizer_sec_1_grp_2(widgs[1]),0,wx.ALL|wx.EXPAND,5)

        return szr

    def sizer_sec_1_grp_1(self,widgs):
        '''
        As mention above in the "sec_1_wdg_group_1" method this section contains a group of widgets store in two colums.
        Each row of widgets will be placed in a HORIZONTAL style; and
        Each row will be placed in VERTICAL style on top of each other to form the columns.

        ______________________________________
        | *---------------------------------* |
        | |  Check Btn  | Choice/TextField  | |
        | *---------------------------------* |
        | |  Check Btn  | Choice/TextField  | |
        | *---------------------------------* |
        |_____________________________________|

        '''
        colum = wx.BoxSizer(wx.VERTICAL)
        rows = list()

        #Populate Rows
        for r in range(int(len(widgs)/2)):
            rows.append(wx.BoxSizer(wx.HORIZONTAL))

        counter = 0
        idx = 0
        for wdg in widgs:
            rows[idx].Add(wdg,0,wx.ALL|wx.EXPAND,1)
            counter += 1
            if(counter == 2):
                counter = 0
                idx += 1
                continue

        #Populate Colums
        for rs in rows:
            colum.Add(rs,0,wx.ALL|wx.EXPAND,2)

        return colum

    def sizer_sec_1_grp_2(self,widgs):
        szr = wx.BoxSizer(wx.VERTICAL)
        for wdg in widgs:
            szr.Add(wdg,0,wx.ALL|wx.EXPAND,5)

        return szr

    def sizer_sec_2(self,widgs):
        szr = wx.BoxSizer(wx.VERTICAL)
        szr.Add(widgs[0],0,wx.ALL|wx.EXPAND,5)
        return szr

    def sizer_sec_3(self,widgs):
        szr = wx.BoxSizer(wx.HORIZONTAL)

        for wdg in widgs:
            szr.Add(wdg,0,wx.ALL|wx.EXPAND,5)

        return szr

    '''---------------------------------------------------
                    INTERNAL METHODS
    ---------------------------------------------------'''
    #Determines if the search paramter is emtpy, otherwise return True
    def empty_search_parameter(self):
        for sp in self.Search_Parameter:
            if sp != "":
                return False
        return True
    
    def _Populate_Listctrl(self,data):
        #Add Rows - These are the data obtain from the DB.
        for rws in range(len(data)):
            self.wdgs_2[0].InsertItem(rws,"")
            for clm in range(len(data[rws])):
                self.wdgs_2[0].SetItem(rws,clm,str(data[rws][clm]))


    '''---------------------------------------------------
                    EVENT HANDLER METHODS
    ---------------------------------------------------'''
    #Check Boxes are organized in a list of lists.
    #widgets = [
    #           [ [ChbX],[Choice], [ChbX],[Text], [ChbX],[Date] ], [Search Button]
    #          ]

    # -- Check Box 1 --
    def OnClick_CheckBox1(self,event):
        #Check, CheckBox, is seleceted...
        if self.wdgs_1[0][0].IsChecked():
            #Retrive User Input; "Choices"...
            self.wdgs_1[0][1].Enable(True)
            self.wdgs_1[0][1].Bind(wx.EVT_CHOICE ,self.sp_client)
        else:
            self.wdgs_1[0][1].Enable(False)
            self.Search_Parameter[0]=""

    # -- Check Box 2 --
    def OnClick_CheckBox2(self,event):
        if self.wdgs_1[0][2].IsChecked():
            #Retrive Text Input; "TextCtrl"
            self.wdgs_1[0][3].Enable(True)
            self.wdgs_1[0][3].Bind(wx.EVT_TEXT,self.sp_jobid)
        else:
            self.wdgs_1[0][3].Enable(False)
            self.Search_Parameter[1]=""

    # -- Check Box 3 --
    def OnClick_CheckBox3(self,event):
        if self.wdgs_1[0][4].IsChecked():
            self.wdgs_1[0][5].Enable(True)
            #Retrive Date Selected; "DatePickerCtrl"
            #self.wdgs_1[0][5].Bind(wx.EVT_DATE_CHANGED, self.sp_date)
            print("wx.EVT for DatePickerCtrl Not Working Porperly")
        else:
            self.wdgs_1[0][5].Enable(False)
            self.Search_Parameter[2]=""

    # - Choice -
    def sp_client(self,event):
        if(not self.wdgs_1[0][1].GetSelection() == wx.NOT_FOUND):
            self.Search_Parameter[0] = self.wdgs_1[0][1].GetString(self.wdgs_1[0][1].GetSelection())

    # - TextCtrl -
    def sp_jobid(self,event):
        if(not self.wdgs_1[0][3].GetLineText(0) == ""):
            self.Search_Parameter[1] = self.wdgs_1[0][3].GetLineText(0)

    # - DatePickerCtrl -
    def sp_date(self, event):
        print( self.wdgs_1[0][5].GetValue() )

    # -- Search Button --
    def OnClickSearch(self,event):
        #Once the Search Button is clicked the App will:
            # 1. Check that there is one or more CheckBoxes selected.
            # 2. Based on the CheckBox selected, retrive the data on the Input Area.
            # 3. Submit a Query to the DB in use.
            # 4. Make the ListCtrl display the query results.
            # 5. That is it.

        # ----- 1 -----
        if(self.empty_search_parameter()):
            wx.MessageDialog(self,"PLEASE SELECT A SEARCH PARAMETER.","WARNING", wx.OK | wx.ICON_EXCLAMATION).ShowModal()
        else:
            query_result = self.db_acc.get_data(set_search_parameters(self.Search_Parameter))
            #DeleteAllItems
            self.wdgs_2[0].DeleteAllItems()
            
            self._Populate_Listctrl(query_result)
    
    def OnClickClearSearch(self,event):
        #Uncheck Check Buttons
        self.wdgs_1[0][0].SetValue(False)
        self.wdgs_1[0][2].SetValue(False)
        self.wdgs_1[0][4].SetValue(False)
        
        #Clear Content of all Paremeters options.
        self.wdgs_1[0][1].Enable(False)
        self.wdgs_1[0][3].Enable(False)
        self.wdgs_1[0][5].Enable(False)
        self.Search_Parameter=["","",""]

        #Clear and Populate ListCtrl with all the records
        self.wdgs_2[0].DeleteAllItems()
        self._Populate_Listctrl(self.db_acc.get_data(set_search_parameters(self.Search_Parameter)))


            




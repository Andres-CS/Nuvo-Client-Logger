#Gui -> User Input Section.

import wx
import wx.lib.scrolledpanel as scrolled

from .Dialogs.NewClientDialog import newclient_dialog
from .Dialogs.ProfileDialog import profiles_dlg
from .Dialogs.ResultDialog import result_Dialog
from Client.ClientMgt import get_clients
from Profiles.paperPfl import paperPfl
from .FormUserDataCheck import form_missingdata, form_checkDatatype, form_correctDataType
from programALU import ALU


class formPanel(scrolled.ScrolledPanel):
    def __init__(self,parent, Labels_for_UserForm):

        #Initialize wx.Panel
        M_Panel = scrolled.ScrolledPanel.__init__(self,parent,-1)
        '''------------------------------------------------------------
                          Declaration of Sections
        ------------------------------------------------------------'''
        #----------Section 1 - Elements--------------
        self.sec_0_labels = Labels_for_UserForm[0]
        #----------Section 1 - Elements--------------
        self.sec_1_labels = Labels_for_UserForm[1]
        #----------Section 2 - Elements--------------
        self.sec_2_labels = Labels_for_UserForm[2]
        #----------Section 3 - Elements--------------
        self.sec_3_labels = Labels_for_UserForm[3]
        #----------Section 4 - Elements--------------
        self.sec_4_labels = Labels_for_UserForm[4]
        #----------Submit Button Section--------------
        self.submitSection = Labels_for_UserForm[5]
        #------------Sizers - Elements----------------
        sec_0_sizer = list()
        sec_1_sizer = list()
        sec_2_sizer = list()
        sec_3_sizer = list()
        sec_4_sizer = list()
        submitsection = list()

        App_sizer = wx.BoxSizer(wx.VERTICAL)

        '''------------------------------------------------------------
                                Creation of Sections
        ------------------------------------------------------------'''
        self.sec_0_widgets = self.section_0(self.sec_0_labels)
        self.sec_1_widgets = self.section_1(self.sec_1_labels)
        self.sec_2_widgets = self.section_2(self.sec_2_labels)
        self.sec_3_widgets = self.section_3(self.sec_3_labels)
        self.sec_4_widgets = self.section_4(self.sec_4_labels)
        self.sec_submit = self.section_submit(self.submitSection)
        '''------------------------------------------------------------
                               Section Line Separator
        ------------------------------------------------------------'''
        self.section_line_separator=list()
        #RANGE IS INPUT HARD-CODED BY THE CODER BASED ON THE NUMBER OF SECTIONS CREATED
        for num_of_sections in range(5):
            self.section_line_separator.append(self.InsertSeparatorLine("h"))
        
        '''------------------------------------------------------------
                                Setting of Sizers
        ------------------------------------------------------------'''
        sec_0_sizer = self.set_sizers_section_0()
        sec_1_sizer = self.set_sizers_section_1()
        sec_2_sizer = self.set_sizers_section_2()
        sec_3_sizer = self.set_sizers_section_3()
        sec_4_sizer = self.set_sizers_section_4()
        submitsection = self.set_sizers_submit()

        App_sizer.Add(sec_0_sizer,0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(self.section_line_separator[0],0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(sec_1_sizer,0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(self.section_line_separator[1],0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(sec_2_sizer,1,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(self.section_line_separator[2],0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(sec_3_sizer,1,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(self.section_line_separator[3],0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(sec_4_sizer,1,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(self.section_line_separator[4],0,wx.ALL | wx.EXPAND,5)
        App_sizer.Add(submitsection,1,wx.ALL | wx.EXPAND,5)

        self.SetSizer(App_sizer)

        self.SetupScrolling()

        '''------------------------------------------------------------
                                Binding of Widgets
        ------------------------------------------------------------'''
        #Button Bindings
        self.sec_0_widgets[2].Bind(wx.EVT_BUTTON,self.onclick_newclient)
        self.sec_3_widgets[3].Bind(wx.EVT_BUTTON,self.onClick_paper_profile)
        self.sec_submit[0].Bind(wx.EVT_BUTTON,self.onClick_Submitt_Button)

    '''
        ---------- SECTION METHODS ------------
    '''
    def section_0(self,labels):
        sec_0_objs = list()
        #Crate Label for clients
        sec_0_objs.append(self.InserLabel(labels[0],(50,15)))
        #Create Choice Widget
        sec_0_objs.append(self.InsertChoices(labels[1]))
        #Create Button for new Client
        sec_0_objs.append(self.InsertButton(labels[2]))

        return sec_0_objs



    '''Returns: list of lists'''
    def section_1(self, fields):
        sec_1_objs = list()

        #Populate Section 1
        for item in fields:
            label = self.InserLabel(item,(100,15)) #LABEL
            text = self.InsertText()         #TEXT-CTL

            sec_1_objs.append( [label, text] )

        return sec_1_objs

    '''Returns: a list of wx widgets'''
    def section_2(self, fields):
        sec_2_objs = list()

        #Sec 2 Title
        sec_2_objs.append(self.InserLabel(fields[0]))

        for sec_2_item in fields[1:]:
            #Sec 2 Buttons
            sec_2_objs.append(self.InsertRadioButton(sec_2_item))

        return sec_2_objs

    '''Returns: a list of wx widgets'''
    def section_3(self,labels):
        sec_3_objs = list()
        #Crater Sub-Title Section
        sec_3_objs.append(self.InserLabel(labels[0]))
        #Label for Paper CHOICES
        sec_3_objs.append(self.InserLabel(labels[1],(50,15)))
        #Create Choices for PAPER profile widget.
        sec_3_objs.append(self.InsertChoices(labels[2]))
        #Insert Button to check out profile specs.
        sec_3_objs.append(self.InsertButton(labels[3]))
        #Label for Printer CHOICES
        sec_3_objs.append(self.InserLabel(labels[4],(50,15)))
        #Create Choices for PRINTER profile widget.
        sec_3_objs.append(self.InsertChoices(labels[5]))
        #Insert Button to check out profile specs.
        sec_3_objs.append(self.InsertButton(labels[6]))

        return sec_3_objs

    '''Returns: a list of wx widgets'''
    def section_4(self, labels):
        #Main list containing all groups of widgets
        sec_4_obj = list()
        #List of wdigets groups.
        #Section 4.1 for Bindig Options
        sec_4_1_objs = list()
        #Section 4.2 for Insert Pages Option
        sec_4_2_objs = list()

        #Create Title Section
        sec_4_obj.append(self.InserLabel(labels[0]))

        ''' Section 4.1'''
        #Title
        sec_4_1_objs.append(self.InserLabel(labels[1]))
        #Choice Options
        sec_4_1_objs.append(self.InsertChoices(labels[2]))
        ''' Section 4.2'''
        #Title
        sec_4_2_objs.append(self.InserLabel(labels[3]))
        #Spin Ctl Option
        sec_4_2_objs.append(self.InsertSpinControlDouble("0"))

        #Merge widgets objects
        sec_4_obj.append(sec_4_1_objs)
        sec_4_obj.append(sec_4_2_objs)

        return sec_4_obj

    ''''Returns: a list of wx widgets'''
    def section_submit(self,labels):
        sec_sbtBttn = list()
        #Create Submition Buttons
        sec_sbtBttn.append(self.InsertButton(labels[0]))
        return sec_sbtBttn

    '''
        ---------- SIZER METHODS ------------
    '''

    def set_sizers_section_0(self):
        group_sizer = wx.BoxSizer(wx.HORIZONTAL)
        for wdgs in self.sec_0_widgets:
            group_sizer.Add(wdgs,0,wx.ALL,5)

        return group_sizer

    ''' Create Sizer for Section_1'''
    def set_sizers_section_1(self):
        group_sizer = list()
        widget_Label= list()
        widget_Text = list()

        #Create n BoxSizers for n num of  self.sec_1_widgets.
        #An object is each line that consists of a Label:Input
        for num in range(len(self.sec_1_widgets)):
            group_sizer.append(wx.BoxSizer(wx.HORIZONTAL))

        #Extract each n num of widgets and place them in the
        #appropiate list. Thus creating a list full of widgets(wx.objects).
        for pairs in  self.sec_1_widgets:
            widget_Label.append(pairs[0])
            widget_Text.append(pairs[1])

        #From the widgets lists, add each widget(label, text) to the
        #HORIZONTAL BoxSizer object.
        for n in range(len(group_sizer)):
            group_sizer[n].Add(widget_Label[n],0,wx.ALL,5)
            group_sizer[n].Add(widget_Text[n],1,wx.ALL|wx.EXPAND,5)

        #Section 1 Sizer Wrapper
        section_1 = wx.BoxSizer(wx.VERTICAL)

        #Add each one of the HORIZONTAL BoxSizers to the VERTICAL BoxSizer.
        #Thus the H.BoxSizers will be added in stack-like style.
        for i in group_sizer:
            section_1.Add(i,0,wx.ALL | wx.EXPAND,5)

        #Return the over all Section1 BoxSizer
        #S1.BoxSizer [ h.BoxSizer, h.BoxSizer, ... ]
        return section_1

    '''Create Sizer for Section_2'''
    def set_sizers_section_2(self):
        section_2 = wx.BoxSizer(wx.VERTICAL)
        group_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #Sub-Section2.1 - Siding Title
        section_2.Add(self.sec_2_widgets[0],0,wx.ALL,5)

        #Sub-Section2.2 - Buttons
        print()
        for i in range(len(self.sec_2_widgets)):
            #THIS COULD BE CODED IN A BETTER WAY WITH ARRAY SLICING | TRY TO FIX!!
            if(i == 0):
                continue
            group_sizer.Add(self.sec_2_widgets[i],0,wx.ALL,5)

        section_2.Add(group_sizer,0,wx.ALL,0)

        return section_2

    '''Create Sizer for Section_3'''
    def set_sizers_section_3(self):
        #Sizer within section 3
        group_sizer = wx.BoxSizer(wx.VERTICAL)
        #Sizers for the Drop down Menu (choice widget) and button
        paper_ch_bt =  wx.BoxSizer(wx.HORIZONTAL)
        printer_ch_bt =  wx.BoxSizer(wx.HORIZONTAL)

        #Adding Widgets to the sizers
        #First is the title widget, which means index position zero
        group_sizer.Add(self.sec_3_widgets[0],0,wx.ALL,0)
        #Paper widgets are the label, menu and button, index position 1, 2 and 3.
        for i in range(len(self.sec_3_widgets)):
            if(i == 0):
                continue
            elif(i in [1,2,3]):
                paper_ch_bt.Add(self.sec_3_widgets[i],0,wx.ALL,0)
            else:
                printer_ch_bt.Add(self.sec_3_widgets[i],0,wx.ALL,0)

        #Grouping all sizer
        group_sizer.Add(paper_ch_bt,0,wx.ALL,5)
        group_sizer.Add(printer_ch_bt,0,wx.ALL,5)

        return group_sizer

    '''Create Sizer for Section_4'''
    def set_sizers_section_4(self):
        #Section 4 iS compose of 2 sublist of widgets.
        # Main sizer
        group_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Submain sizers
        sizer_4_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4_2 = wx.BoxSizer(wx.VERTICAL)

        #Title sectoin sizer
        group_sizer.Add(self.sec_4_widgets[0])

        #Group 1 sizer
        for i in self.sec_4_widgets[1]:
            sizer_4_1.Add(i,0,wx.ALL,0)

        #Group 2 sizer
        for j in self.sec_4_widgets[2]:
            sizer_4_2.Add(j,0,wx.ALL,0)

        #Group all sizer of section 4
        group_sizer.Add(sizer_4_1,0,wx.ALL,5)
        group_sizer.Add(sizer_4_2,9,wx.ALL,5)

        return group_sizer


    '''Create Sizer for Section_submit'''
    def set_sizers_submit(self):
        group_sizer=wx.BoxSizer(wx.VERTICAL)
        #Create Sizer for submition button
        group_sizer.Add(self.sec_submit[0],0,wx.ALL|wx.CENTER,0)

        return group_sizer


    '''
        ---------- WIDGET METHODS ------------
    '''
    def InserLabel(self,label,size=wx.DefaultSize):
       return wx.StaticText(self,-1,label,size=size)

    def InsertText(self):
        return wx.TextCtrl(self,-1,'')

    def InsertRadioButton(self,label):
        return wx.RadioButton(self,-1,label=label)

    def InsertButton(self,label,pos=(0,0)):
        return wx.Button(self,wx.ID_ANY,label,pos=pos)

    def InsertChoices(self,choicestochose):
        return wx.Choice(self,-1,choices=choicestochose, style=wx.CB_SORT)

    def InsertSpinControlDouble(self,dv="0"):
        return wx.SpinCtrlDouble(self,-1,value=dv,style= wx.SP_ARROW_KEYS,min=0,max=1000,inc=1)

    def InsertSeparatorLine(self,style_h_v="v"):
        if style_h_v.lower() == "h":
            return wx.StaticLine(self,wx.ID_ANY,style=wx.HORIZONTAL)
        return wx.StaticLine(self,wx.ID_ANY,style=wx.VERTICAL)

    '''
        ---------- DATA PARSING ------------
    '''

    def form_collect_user_data(self):
        '''
            Please keep in mind that the keys for dict DATA, must match DB fields.
        '''
        #FOR TEST
        print(" - COLLECTING DATA - ")

        #Data inputed or selected by the user.
        DATA = dict()

        #Collect Client Selected
        DATA["Client"]=self.sec_0_widgets[1].GetString(self.sec_0_widgets[1].GetSelection())

        #Collect Text Fields
        for item in range(len(self.sec_1_widgets)):
            #sec_1_labels -> [ wxlabel, , ]
            if self.sec_1_labels[item] not in DATA:
                #DATA[LABEL]=VALUE
                DATA[self.sec_1_labels[item]] = self.sec_1_widgets[item][1].GetLineText(0)

        #Collect Siding. Siding will be stored in a list form.
        if(self.sec_2_widgets[1].GetValue() == True):
            DATA['Siding'] = 1
        elif(self.sec_2_widgets[2].GetValue() == True):
            DATA['Siding'] = 2

        #Collect type of Paper, Paper choice widget with index 2
        DATA["Paper"] = self.sec_3_widgets[2].GetString(self.sec_3_widgets[2].GetSelection())

        #Collect type of Printer, Printer choice widget with index 5
        DATA["Printer"] = self.sec_3_widgets[5].GetString(self.sec_3_widgets[5].GetSelection())

        #Collect type of Spiral Binding | wx.Choice widget with index [1][1]
        DATA["Coil"] = self.sec_4_widgets[1][1].GetString(self.sec_4_widgets[1][1].GetSelection())

        #Collect Inserts | wx.SpinControlDouble widget with indec [2][1]
        DATA["Inserts"] = self.sec_4_widgets[2][1].GetValue()

        
        
        #FOR TEST
        for k in DATA:
            print(k,end=": ")
            print(DATA[k])



        return DATA
    

    '''
        ---------- EVNT HANDLER METHODS ------------
    '''
    def onclick_newclient(self,event):
        newclient_dialog()
        #Update Choice options
        self.sec_0_widgets[1].Clear()
        self.sec_0_widgets[1].AppendItems(get_clients())

    def sec_3_paper_choice_hdlr(self,event):
        #Store profile selected by user
        selection = self.sec_3_widgets[2].GetString(self.sec_3_widgets[2].GetSelection())
        #Run Dialog showing profile specs
        profiles_dlg(paperPfl().get_profileAttr(selection))

    def onClick_paper_profile(self, event):
        #Check if an option from choice has been selected.
        if(self.sec_3_widgets[2].GetSelection() == -1):
            wx.MessageDialog(self,"NO OPTION SELECTED YET","WARNING", wx.OK | wx.ICON_EXCLAMATION).ShowModal()
        else:
            self.Bind(wx.EVT_CHOICE, self.sec_3_paper_choice_hdlr(event),self.sec_3_widgets[2])

    #Submitt Button Handler
    def onClick_Submitt_Button(self,event):

        PAYLOAD = {
            "CRUD":"CREATE",
            "PAYLOAD": dict()
        }
        #User DATA and RESULTS
        userData = dict()
        resultData = dict()

        #Check there is no missing DATA
        if(form_missingdata(self.sec_0_widgets,self.sec_1_widgets,self.sec_2_widgets,self.sec_3_widgets,self.sec_4_widgets) == True):
            wx.MessageDialog(self,"PLEASE COMPLETE\nALL MISSING DATA.","WARNING", wx.OK | wx.ICON_EXCLAMATION).ShowModal()
        else:
            #Collect data entered by user
            userData = self.form_collect_user_data()
            userDATA = form_correctDataType(userData)

            PAYLOAD["PAYLOAD"]["userData"] = userDATA

            #Test data' dataype
            if(form_checkDatatype(userData) == True):
                resultData = ALU(userData)
                PAYLOAD["PAYLOAD"]["resultData"]= resultData

                #SEND TO RESULT DIALOG
                result_Dialog(PAYLOAD)

            else:
                wx.MessageDialog(self,"PLEASE INSERT\nTHE CORRECT DATATYPE.","WARNING", wx.OK | wx.ICON_EXCLAMATION).ShowModal()

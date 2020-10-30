#Dialog for Results of Calculation.

import wx

from App_DB_Bridge import databaseBridge as Bridge

'''
    ---------- RESULT DIALOG ------------
'''
class resultDialog(wx.Dialog):
    def __init__(self,PAYLOAD):
        super(resultDialog,self).__init__(None,wx.ID_ANY,"Results")

        #labels
        self.data_to_display = list()
        self.num_labels = 0

        #Dialgo Panel
        result_dg_panel = wx.Panel(self,wx.ID_ANY,size=(600,700))
        #Dialog SataticText Widgets
        st_widgets = list()
        #Dialog BoxSizer
        dg_bx_sizer = wx.BoxSizer(wx.VERTICAL)

        #Setting up data to be display for dialog.
        self.data_to_display, self.num_labels = self.prepare_labels(PAYLOAD["PAYLOAD"]["userData"], PAYLOAD["PAYLOAD"]["resultData"])

        #Create Widgets
        for i in range(self.num_labels):
            st_widgets.append(wx.StaticText(result_dg_panel,wx.ID_ANY,self.data_to_display[i]))

        #Create Sizers for Widgets
        for ii in range(self.num_labels):
            dg_bx_sizer.Add(st_widgets[ii],0,wx.ALL,0)
        
        #Create "Save Data" Radio Button
        SaveDataRadioButton = wx.RadioButton(self,wx.ID_ANY,label="SAVE DATA?")

        #Add it to the BoxSizer
        dg_bx_sizer.Add(SaveDataRadioButton,0,wx.ALL,3)

        '''MAKE BOX TO SAVE THAT by USER CHOICE'''
        print('---- TESTING -----')
        obj = Bridge()
        obj.send2DB(PAYLOAD)


    def prepare_labels(self,userData,resultData):
        dg_labels=list()

        #Extract userData & resultData keys
        ud_keys = list(userData.keys())
        rd_keys = list(resultData.keys())

        ud_value=list()
        rd_value=list()
       
        #Extract values from userData & resultData
        for ud_key in ud_keys:
            ud_value.append(userData[ud_key])
        for rd_key in rd_keys:
            rd_value.append(resultData[rd_key])

        #Concatenate Labels
        for i in range(len(ud_keys)):
            tmp = ud_keys[i]+": "+str(ud_value[i])
            dg_labels.append(tmp)
        for ii in range(len(rd_keys)):
            tmp = rd_keys[ii]+": "+str(rd_value[ii])
            dg_labels.append(tmp)

        return dg_labels, len(dg_labels)

'''
    ----------- RUN RESULT DIALOG ------------
'''

def result_Dialog(PAYLOAD):
    RtDlg = resultDialog(PAYLOAD)
    RtDlg.ShowModal()
    RtDlg.Destroy()

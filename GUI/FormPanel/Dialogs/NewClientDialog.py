#Dialog for new Client

import wx

from Client.ClientMgt import set_client

class newclient_dlg(wx.Dialog):
    def __init__(self):
        super(newclient_dlg,self).__init__(None,wx.ID_ANY,"New Client")

        self.set_panel()
    
    def set_panel(self):
        #Dlg Panel
        self.nc_panel = wx.Panel(self,-1,size=(10,10))
        
        #Elements
        self.nc_label = wx.StaticText(self.nc_panel,-1,"Enter name of new client: ")
        self.nc_txtctl = wx.TextCtrl(self.nc_panel,-1,)
        self.nc_savebutton = wx.Button(self.nc_panel,-1," Save ")
        
        #Sizers
        self.nc_boxszr = wx.BoxSizer(wx.HORIZONTAL)

        #Adding to Sizer
        self.nc_boxszr.Add(self.nc_label,0,wx.ALL,5)
        self.nc_boxszr.Add(self.nc_txtctl,0,wx.ALL,5)
        self.nc_boxszr.Add(self.nc_savebutton,0,wx.ALL,5)

        self.nc_panel.SetSizer(self.nc_boxszr)

        #--- Binding ---
        self.nc_savebutton.Bind(wx.EVT_BUTTON,self.onclick_savebutton)
        self.nc_savebutton.Bind(wx.EVT_CLOSE,self.onclick_close)

    def onclick_savebutton(self,event):
        client_name = self.nc_txtctl.GetLineText(0)
        set_client(client_name)
        #Close Dialog once Save button has been pressed.
        self.onclick_close()

    def onclick_close(self):
        self.Destroy()


def newclient_dialog():
    nc_dlg = newclient_dlg()
    nc_dlg.ShowModal()
    nc_dlg.Destroy()

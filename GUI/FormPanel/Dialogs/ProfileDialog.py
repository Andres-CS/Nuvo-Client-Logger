#This is the Paper Profile Dialog
import wx

class profile_dlg(wx.Dialog):
    def __init__(self,dg_tittle,attrs):
        super(profile_dlg,self).__init__(None,wx.ID_ANY,dg_tittle)
        #Populate Dialog
        self.dg_panel(attrs)
    
    def dg_panel(self,profile):
        pnl = wx.Panel(self,wx.ID_ANY)

        #Memeber Vars
        row = list()
        col = wx.BoxSizer(wx.VERTICAL)
        
        #Create x num of BoxSizer for x num of Attributes
        for i in range(len(profile)):
            row.append(wx.BoxSizer(wx.HORIZONTAL))
        
        #Create Widges
        index = 0 
        for attr in profile:
            attrb = wx.StaticText(pnl,wx.ID_ANY,str(attr))
            value = wx.StaticText(pnl, wx.ID_ANY,str(profile[attr]))
            row[index].Add(attrb,0,wx.ALL)
            row[index].Add(value,0,wx.ALL)
            index += 1

        for i in row:
            col.Add(i,0,wx.ALL,5)

        pnl.SetSizer(col)
        
'''
    Returns: void
    Action: runs a widget dialog shwoing a profile specification.
'''
def profiles_dlg(profile):
    #Dialgo
    prf_dlg = profile_dlg("Profile: "+profile["type_paper"],profile)
    #Displays de Dialog and it requiers the user to exit it before continuing. 
    prf_dlg.ShowModal()
    #Destroy Dialog. Allows to close application properly.
    prf_dlg.Destroy()

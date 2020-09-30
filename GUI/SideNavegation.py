#Tabs Sections

import wx

class tabPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1)

class TabMenu(wx.Notebook):
    def __init__(self,parent):
        wx.Notebook.__init__(self,parent,style=wx.NB_LEFT)
        pass

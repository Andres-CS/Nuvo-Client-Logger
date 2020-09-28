#GUI -> Application Main Frame

import wx


class mainFrame(wx.Frame):
    def __init__(self,parent):
        #Initialize wx.Frame
        wx.Frame.__init__(self,parent,-1,"Paper Calc",size=(700,580))

        #Set up Icon Application
        icon = wx.EmptyIcon()
        bitmap = wx.Bitmap("nuvo.ico",wx.BITMAP_TYPE_ANY)
        icon.CopyFromBitmap(bitmap)
        self.SetIcon(icon)
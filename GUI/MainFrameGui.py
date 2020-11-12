#GUI -> Application Main Frame

import wx
import os


class mainFrame(wx.Frame):
    def __init__(self,parent):
        #Initialize wx.Frame
        wx.Frame.__init__(self,parent,-1,"The Nuvo Group - Job Register",size=(700,580))

        
        #Set up Icon Application
        App_logo = self.get_logo("nuvo.ico")
        icon = wx.EmptyIcon()
        bitmap = wx.Bitmap(App_logo,wx.BITMAP_TYPE_ANY)
        icon.CopyFromBitmap(bitmap)
        self.SetIcon(icon)
    
    def get_logo(self,logoName): 
        Media_Folder = os.path.abspath(os.path.join(os.getcwd(), "Media/"))
        if logoName in os.listdir(Media_Folder):
            logoName = os.listdir(Media_Folder)[os.listdir(Media_Folder).index(logoName)]
        logoName = os.path.join(Media_Folder,logoName)
        return logoName


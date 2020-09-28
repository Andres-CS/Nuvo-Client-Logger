
import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "My app", size=(1024, 768))
        self._panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.list = wx.ListCtrl(self._panel, wx.ID_ANY,
                                style=wx.LC_REPORT 
                                | wx.LC_EDIT_LABELS
                                | wx.LC_SORT_ASCENDING
                                )
        self.list.AppendColumn("C1", width=110)
        self.list.AppendColumn("C2", width=110)

        hbox.Add(self.list, 1, wx.LEFT|wx.TOP|wx.GROW)

        self._panel.SetSizer(hbox)
        
        data = {143571234234: ('first 1', 'first 2'),
                234567456733: ('second 1', 'second 2'),}
        for key, row in data.items():
            index = self.list.InsertItem(1000000, row[0])
            self.list.SetItem(index, 1, row[1])
            self.list.SetItemData(index, key)
            print("Data set: {}, data get: {}".format(key, self.list.GetItemData(index)))

if __name__ == "__main__":
    print("Wx version: %s", wx.version())
    app = wx.App(False)
    main_frame = MainFrame()
    main_frame.Show()
    app.MainLoop()
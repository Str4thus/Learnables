import wx
import wx.grid as gridlib



class LearnableListView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        box = wx.BoxSizer(wx.HORIZONTAL)
		
        self.list = wx.ListCtrl(self, 0, style = wx.LC_REPORT|wx.LC_HRULES) 
        self.list.InsertColumn(0, 'id', width = 65) 
        self.list.InsertColumn(1, 'question', wx.LIST_FORMAT_CENTRE, 300) 
        self.list.InsertColumn(2, 'answer', wx.LIST_FORMAT_CENTRE, 300) 
        self.list.InsertColumn(3, 'correctness (correct_count / times_seen)', wx.LIST_FORMAT_CENTRE, 300) 
        self.list.InsertColumn(4, 'category', wx.LIST_FORMAT_CENTRE, 300) 
            
        box.Add(self.list,1,wx.EXPAND) 
        self.SetSizer(box)

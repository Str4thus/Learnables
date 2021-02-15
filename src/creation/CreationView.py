import wx


class CreationView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
		
        hbox = wx.BoxSizer(wx.HORIZONTAL)
            
        fgs = wx.FlexGridSizer(4, 2, 10, 10)

        question_label = wx.StaticText(self, label="Question") 
        answer_label = wx.StaticText(self, label="Answer") 
        category_label = wx.StaticText(self, label="Category") 

        self.question_input = wx.TextCtrl(self) 
        self.answer_input = wx.TextCtrl(self)
        self.category_input = wx.TextCtrl(self)
        self.submit_button = wx.Button(self, label="Create")

        fgs.AddMany([
            (question_label), 
            (self.question_input, 1, wx.EXPAND), 
            (answer_label), 
            (self.answer_input, 1, wx.EXPAND),
            (category_label), 
            (self.category_input, 1),
            (self.submit_button)
        ])

        fgs.AddGrowableRow(2, 1) 
        fgs.AddGrowableCol(1, 1)  
        hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 15) 
        self.SetSizer(hbox)
import wx

class TrainView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.displayed_text = wx.TextCtrl(
                self, 
                value="#15\nCorrect: 10% (1/10)\n\nQuestion: \n\nIt may be single line or multi-line. Notice that a lot of methods of the text controls are found in the base wx.TextEntry class which is a common base class for wx.TextCtrl and other controls using a single line text entry field (e.g. wx.ComboBox).",
                style=wx.TE_READONLY|wx.TE_CENTER|wx.TE_BESTWRAP|wx.TE_MULTILINE|wx.TE_NO_VSCROLL
        )

        self.correct_button = wx.Button(self, label="Correct")
        self.turn_around_button = wx.Button(self, label="Turn Around")
        self.wrong_button = wx.Button(self, label="Wrong")

        category_label = wx.StaticText(self, label="Category: ") 
        self.category_selector = wx.ComboBox(self, value="any")


        category_hbox = wx.BoxSizer(wx.HORIZONTAL)
        category_hbox.Add(category_label, 0, wx.EXPAND)
        category_hbox.Add(self.category_selector, 2, wx.EXPAND)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(category_hbox, 1, wx.EXPAND)
        vbox.Add(self.turn_around_button, 10, wx.EXPAND)

        inner_grid = wx.GridSizer(1, 3, 0, 0) 
        inner_grid.Add(self.wrong_button, 0, wx.EXPAND)
        inner_grid.Add(vbox, 0, wx.EXPAND)
        inner_grid.Add(self.correct_button, 0, wx.EXPAND)

        grid = wx.GridSizer(2, 1, 0, 0) 
        grid.Add(self.displayed_text, 0, wx.EXPAND)
        grid.Add(inner_grid, 0, wx.EXPAND)
        self.SetSizer(grid)
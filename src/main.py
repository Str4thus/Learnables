import wx
import wx.grid as gridlib

from train import *
from learnablelist import *
from creation import *

from db import DBManager, LearnableManager, CategoryManager


WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 400

class MainFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Learnables", size=(WINDOW_WIDTH,WINDOW_HEIGHT))
 
        self.train_view = TrainView(self)
        self.learnable_list_view = LearnableListView(self)
        self.creation_view = CreationView(self)


        db_manager = DBManager()
        self.train_controller = TrainController(self.train_view, db_manager)
        self.learnable_list_controller = LearnableListController(self.learnable_list_view, db_manager)
        self.creation_controller = CreationController(self.creation_view, db_manager)


        self.learnable_list_view.Hide()
        self.creation_view.Hide()
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.train_view, 1, wx.EXPAND)
        self.sizer.Add(self.learnable_list_view, 1, wx.EXPAND)
        self.sizer.Add(self.creation_view, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        
        menubar = wx.MenuBar()
        nav_menu = wx.Menu()
        training_nav_button = nav_menu.Append(wx.ID_ANY, "Training")
        list_nav_button = nav_menu.Append(wx.ID_ANY, "Learnable List")
        create_nav_button = nav_menu.Append(wx.ID_ANY, "Create...")
    
        self.Bind(wx.EVT_MENU, self.switch_to_training, training_nav_button)
        self.Bind(wx.EVT_MENU, self.switch_to_list, list_nav_button)
        self.Bind(wx.EVT_MENU, self.switch_to_creation, create_nav_button)

        menubar.Append(nav_menu, '&Navigate')
        self.SetMenuBar(menubar)

        
    def switch_to_training(self, event):
        self.learnable_list_view.Hide()
        self.creation_view.Hide()

        self.train_view.Show()
        self.Layout()

    def switch_to_list(self, event):
        self.creation_view.Hide()
        self.train_view.Hide()

        self.learnable_list_view.Show()
        self.Layout()

    def switch_to_creation(self, event):
        self.learnable_list_view.Hide()
        self.train_view.Hide()

        self.creation_view.Show()
        self.Layout()
        
 
if __name__ == "__main__":
    db_man = DBManager()
    category_man = CategoryManager(db_man)
    learnable_man = LearnableManager(db_man)
    
    
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()


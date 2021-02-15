import wx
import wx.grid as gridlib
from viewcontroller import ViewController
from db import DBManager


class LearnableListController(ViewController):
    def __init__(self, view: wx.Panel, db_manager: DBManager):
        ViewController.__init__(self, db_manager)
        self.view = view
        self.view.Bind(wx.EVT_SHOW, self.on_show)
        self.view.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.on_list_right_click)


    def on_show(self, event):
        self._update_list()

    def on_delete(self, event, learnable_id: int):
        self.learnable_manager.remove_learnable(learnable_id)
        self._update_list()

    def on_list_right_click(self, event):
        learnable_id = event.GetText()
        
        popupmenu = wx.Menu()
        menu_item = popupmenu.Append(-1, "Delete")

        wrapper = lambda event: self.on_delete(event, learnable_id)
        self.view.Bind(wx.EVT_MENU, wrapper, menu_item)
        self.view.PopupMenu(popupmenu, event.GetPoint())


    def _update_list(self):
        if self.view.list.GetItemCount() > 0:
            self.view.list.DeleteAllItems()

        for learnable in self.learnable_manager.retrieve_all_learnables():
            category = self.category_manager.retrieve_category_by_id(learnable.get_category_id())
            
            index = self.view.list.InsertItem(51342, learnable.get_id())
            self.view.list.SetItem(index, 0, str(learnable.get_id())) 
            self.view.list.SetItem(index, 1, learnable.get_question()) 
            self.view.list.SetItem(index, 2, learnable.get_answer())

            if learnable.get_times_seen() > 0:
                self.view.list.SetItem(index, 3, str(round((learnable.get_correct_count() / learnable.get_times_seen()) * 100, 2)))
            else:
                self.view.list.SetItem(index, 3, "Not trained yet")

            self.view.list.SetItem(index, 4, category.get_name())
           
            

    
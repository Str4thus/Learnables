import wx
from viewcontroller import ViewController
from db import DBManager


class CreationController(ViewController):
    def __init__(self, view: wx.Panel, db_manager: DBManager):
        ViewController.__init__(self, db_manager)
        self.view = view

        self.view.submit_button.Bind(wx.EVT_BUTTON, self.on_submit)


    def create_new_learnable(self, question: str, answer: str, category_name: str) -> bool:
        if len(question) == 0 or len(answer) == 0 or len(category_name) == 0:
            print("nope")
            return False

        category = self.category_manager.retrieve_category_by_name(category_name)
        if category is None:
            self.category_manager.insert_category(category_name)
            category = self.category_manager.retrieve_category_by_name(category_name)

        self.view.question_input.Clear()
        self.view.answer_input.Clear()
        self.view.category_input.Clear()

        return self.learnable_manager.insert_learnable(question, answer, category)
        


    def on_submit(self, event):
        self.create_new_learnable(self.view.question_input.GetValue(), self.view.answer_input.GetValue(), self.view.category_input.GetValue())
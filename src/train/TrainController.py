import wx
import random
from typing import List
from viewcontroller import ViewController
from db import DBManager, Learnable


class TrainController(ViewController):
    def __init__(self, view: wx.Panel,  db_manager: DBManager):
        ViewController.__init__(self, db_manager)
        self.view = view
        self.view.correct_button.Bind(wx.EVT_BUTTON, self.on_correct)
        self.view.wrong_button.Bind(wx.EVT_BUTTON, self.on_wrong)
        self.view.turn_around_button.Bind(wx.EVT_BUTTON, self.on_turn_around)
        self.view.category_selector.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.on_dropdown_open)

        self.current_learnable = self._select_learnable(self.learnable_manager.retrieve_all_learnables())
        self.is_showing_question = True

        self._update_displayed_text()


    def on_correct(self, event):
        if self.current_learnable is None:
            self.next()
            return
        
        self.learnable_manager.update_learnable(self.current_learnable.get_id(), self.current_learnable.get_correct_count() + 1, self.current_learnable.get_times_seen() + 1)
        self.next()

    def on_wrong(self, event):
        if self.current_learnable is None:
            self.next()
            return

        self.learnable_manager.update_learnable(self.current_learnable.get_id(), self.current_learnable.get_correct_count(), self.current_learnable.get_times_seen() + 1)
        self.next()

    def on_dropdown_open(self, event) -> None:
        self._update_category_selector()


    def on_turn_around(self, event) -> None:
        self.is_showing_question = not self.is_showing_question
        self._update_displayed_text()


    def next(self):
        category_string = self.view.category_selector.GetValue()
        if "any" in category_string:
            self.current_learnable = self._select_learnable(self.learnable_manager.retrieve_all_learnables())
        else:
            category = self.category_manager.retrieve_category_by_name(category_string)
            self.current_learnable = self._select_learnable(self.learnable_manager.retrieve_learnables_by_category(category))

        self._update_displayed_text()

    def _select_learnable(self, learnables: List[Learnable]) -> Learnable:
        if len(learnables) == 0:
            return None
        
        return random.choice(learnables)

    def _update_displayed_text(self) -> None:
        if self.current_learnable is None:
            updated_text = "No learnables available!"
        else:
            updated_text = "#{}\nCorrect: {} ({}/{})\n\n{}: \n\n{}".format(
                self.current_learnable.get_id(),
                str(round((self.current_learnable.get_correct_count() / self.current_learnable.get_times_seen()) * 100, 2)) + "%" if self.current_learnable.get_times_seen() > 0 else "Not trained yet",
                self.current_learnable.get_correct_count(),
                self.current_learnable.get_times_seen(),
                "Question" if self.is_showing_question else "Answer",
                self.current_learnable.get_question() if self.is_showing_question else self.current_learnable.get_answer()
            )

        self.view.displayed_text.SetValue(updated_text)

    def _update_category_selector(self) -> None:
        self.view.category_selector.Clear()
        self.view.category_selector.Append("any")
        self.view.category_selector.SetValue("any")

        for category in self.category_manager.retrieve_all_categories():
            if len(self.learnable_manager.retrieve_learnables_by_category(category)) == 0:
                self.category_manager.remove_category(category.get_id())
            else:
                self.view.category_selector.Append(category.get_name())
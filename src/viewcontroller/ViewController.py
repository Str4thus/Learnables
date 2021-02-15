from db import DBManager, LearnableManager, CategoryManager


class ViewController(object):
    def __init__(self, db_manager: DBManager):
        self.learnable_manager = LearnableManager(db_manager)
        self.category_manager = CategoryManager(db_manager)
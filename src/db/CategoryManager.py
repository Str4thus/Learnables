from .DBManager import DBManager, CategoryContract
from .models import Category
from typing import List, Union


class CategoryManager(object):
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager


    def retrieve_all_categories(self) -> List[Category]:
        query = "SELECT * FROM {}".format(
            CategoryContract.TABLE_NAME.value
            )
        
        categories = []
        for row in self.db_manager.query(query):
            categories.append(self._create_category_instance(row))

        return categories

    def retrieve_category_by_id(self, category_id: int) -> Category:
        query = "SELECT * FROM {} WHERE {}=?".format(
            CategoryContract.TABLE_NAME.value,
            CategoryContract.COLUMN_ID.value,
        )

        params = (category_id,)
        result = self.db_manager.query(query, params)
        if len(result) == 0:
            return None

        return self._create_category_instance(result[0])

    def retrieve_category_by_name(self, name: str) -> Category:
        query = "SELECT * FROM {} WHERE {}=?".format(
            CategoryContract.TABLE_NAME.value,
            CategoryContract.COLUMN_NAME.value,
        )

        params = (name,)
        result = self.db_manager.query(query, params)
        if len(result) == 0:
            return None

        return self._create_category_instance(result[0])


    def insert_category(self, name: str) -> bool:
        query = "INSERT INTO {}({}) VALUES (?)".format(
            CategoryContract.TABLE_NAME.value,
            CategoryContract.COLUMN_NAME.value
            )
        
        params = (name,)
        
        if self.db_manager.query(query, params):
            return False
        return True


    def remove_category(self, category_id: int) -> None:
        query = "DELETE FROM {} WHERE {}=?".format(
            CategoryContract.TABLE_NAME.value,
            CategoryContract.COLUMN_ID.value,
        )

        params = (category_id,)
        self.db_manager.query(query, params)

    def _create_category_instance(self, data: tuple) -> Category:
        return Category(data[0], data[1])

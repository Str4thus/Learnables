from .DBManager import DBManager, LearnableContract
from .models import Learnable, Category
from typing import List


class LearnableManager(object):
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager


    def retrieve_all_learnables(self) -> List[Learnable]:
        query = "SELECT * FROM {}".format(
            LearnableContract.TABLE_NAME.value
        )
        
        learnables = []
        for row in self.db_manager.query(query):
            learnables.append(self._create_learnable_instance(row))
        
        return learnables

    def retrieve_learnable_by_id(self, learnable_id: int) -> Learnable:
        query = "SELECT * FROM {} WHERE {}=?".format(
            LearnableContract.TABLE_NAME.value,
            LearnableContract.COLUMN_ID.value,
        )

        params = (learnable_id,)
        result = self.db_manager.query(query, params)
        if len(result) == 0:
            return None

        return self._create_learnable_instance(result[0])

    def retrieve_learnables_by_category(self, category: Category) -> List[Learnable]:
        query = "SELECT * FROM {} WHERE {}=?".format(
            LearnableContract.TABLE_NAME.value,
            LearnableContract.COLUMN_CATEGORY.value
        )

        params = (category.get_id(),)

        learnables = []
        for row in self.db_manager.query(query, params):
            learnables.append(self._create_learnable_instance(row))
        
        return learnables


    def insert_learnable(self, question: str, answer: str, category: Category) -> bool:
        query = "INSERT INTO {}({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(
            LearnableContract.TABLE_NAME.value,
            LearnableContract.COLUMN_QUESTION.value,
            LearnableContract.COLUMN_ANSWER.value,
            LearnableContract.COLUMN_CATEGORY.value,
            
            LearnableContract.COLUMN_CORRECT_COUNT.value,
            LearnableContract.COLUMN_TIMES_SEEN.value
        )
        
        params = (question, answer, category.get_id(), 0, 0)

        if self.db_manager.query(query, params):
            return False
        return True

    def update_learnable(self, learnable_id: int, correct_count: int, times_seen: int) -> bool:
        query = "UPDATE {} SET {}=?, {}=? WHERE {}=?".format(
            LearnableContract.TABLE_NAME.value,
            LearnableContract.COLUMN_CORRECT_COUNT.value,
            LearnableContract.COLUMN_TIMES_SEEN.value,
            LearnableContract.COLUMN_ID.value,
        )
    
        params = (correct_count, times_seen, learnable_id)
        return self.db_manager.query(query, params)

    def remove_learnable(self, learnable_id: int) -> None:
        query = "DELETE FROM {} WHERE {}=?".format(
            LearnableContract.TABLE_NAME.value,
            LearnableContract.COLUMN_ID.value,
        )
    
        params = (learnable_id,)
        self.db_manager.query(query, params)


    def _create_learnable_instance(self, data: tuple) -> Learnable:
        return Learnable(data[0], data[1], data[2], data[3], data[4], data[5])
    
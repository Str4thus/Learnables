import os
import sqlite3 as sqlite

from typing import Union
from enum import Enum


DB_NAME = "learnables"


class CategoryContract(Enum):
    TABLE_NAME="categories"
    COLUMN_ID="category_id"
    COLUMN_NAME="name"

class LearnableContract(Enum):
    TABLE_NAME="learnables"
    COLUMN_ID="learnable_id"
    COLUMN_CORRECT_COUNT="correct_count"
    COLUMN_TIMES_SEEN="times_seen"
    COLUMN_QUESTION="question"
    COLUMN_ANSWER="answer"
    COLUMN_CATEGORY="category"


class DBManager(object):

    def __init__(self):
        self._init_database()
        self._create_tables_if_not_exists()

    def _init_database(self) -> None:
        self.connection = sqlite.connect(DB_NAME + ".db")
        self.cursor = self.connection.cursor()

    def _create_tables_if_not_exists(self) -> None:
        try:
            sql_create_category_table = "CREATE TABLE {} (\
                    {} INTEGER PRIMARY KEY, \
                    {} TEXT NOT NULL,\
                    UNIQUE({})\
                )".format(
                    CategoryContract.TABLE_NAME.value,
                    CategoryContract.COLUMN_ID.value,
                    CategoryContract.COLUMN_NAME.value,
                    CategoryContract.COLUMN_NAME.value,
                )


            sql_create_learnable_table = "CREATE TABLE {} (\
                    {} INTEGER PRIMARY KEY,\
                    {} INTEGER NOT NULL,\
                    {} INTEGER NOT NULL,\
                    {} TEXT NOT NULL,\
                    {} TEXT NOT NULL,\
                    {} INTEGER NOT NULL,\
                    FOREIGN KEY ({}) REFERENCES {} ({})\
                )".format(
                    LearnableContract.TABLE_NAME.value,
                    LearnableContract.COLUMN_ID.value,
                    LearnableContract.COLUMN_CORRECT_COUNT.value,
                    LearnableContract.COLUMN_TIMES_SEEN.value,
                    LearnableContract.COLUMN_QUESTION.value,
                    LearnableContract.COLUMN_ANSWER.value,
                    LearnableContract.COLUMN_CATEGORY.value,
                    LearnableContract.COLUMN_CATEGORY.value,
                    CategoryContract.TABLE_NAME.value,
                    CategoryContract.COLUMN_ID.value
                    )

            
            self.cursor.execute("PRAGMA foreign_keys") # Enable FKs
            self.cursor.execute(sql_create_category_table)
            self.cursor.execute(sql_create_learnable_table)

        except sqlite.OperationalError: # Tables already exists
            pass

    def query(self, query_string: str, params: tuple=()) -> Union[list, int]:
        """
            returns the query result on success or -1 on error
        """
        try:
            self.cursor.execute(query_string, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except sqlite.IntegrityError:
            return -1

from .Category import Category


class Learnable(object):
    def __init__(self, 
        learnable_id: int, 
        correct_count: int, 
        times_seen: int, 
        question: str,
        answer: str,
        category_id: int  
    ):
        self._learnable_id = learnable_id
        self._question = question
        self._answer = answer
        self._correct_count = correct_count
        self._times_seen = times_seen
        self._category_id = category_id


    def get_id(self) -> int:
        return self._learnable_id

    def get_question(self) -> str:
        return self._question

    def get_answer(self) -> str:
        return self._answer

    def get_correct_count(self) -> int:
        return self._correct_count

    def get_times_seen(self) -> int:
        return self._times_seen

    def get_category_id(self) -> int:
        return self._category_id
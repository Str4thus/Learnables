class Category(object):
    def __init__(self, category_id: int, name: str):
        self._category_id = category_id
        self._name = name


    def get_id(self) -> int:
        return self._category_id

    def get_name(self) -> str:
        return self._name
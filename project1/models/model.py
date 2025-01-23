# model.py
class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Model:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

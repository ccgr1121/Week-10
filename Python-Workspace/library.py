import item
class Library:
    def __init__(self):
        self._items = {}
    
    def add_item(self, item:Item):
        self.items[item.id] = item
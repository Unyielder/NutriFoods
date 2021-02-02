class Meal:
    def __init__(self):
        self.food_list = []
        self.macro_ratio = None

    def add_item(self, item):
        self.food_list.append(item)

    def remove_item(self, item):
        pass

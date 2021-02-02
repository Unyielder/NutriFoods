from collections import defaultdict


class Food:
    def __init__(self):
        self.name = ''
        self.measure = ''
        self.calories = None
        self.proteins = None
        self.fat = None
        self.sat_fat = None
        self.fiber = None
        self.carbs = None

    def load_measure(self, result_set):
        self.measure = [res[2] for res in result_set]

    def load_food(self, result_set):
        macros = defaultdict(list)

        self.name = result_set[0][1]
        self.measure = result_set[0][2]

        for res in result_set:
            macros[res[3]].append(res[4])
            macros[res[3]].append(res[5])

        self.calories = macros['CARBOHYDRATE, TOTAL (BY DIFFERENCE)']
        self.proteins = macros['PROTEIN']
        self.fat = macros['FAT (TOTAL LIPIDS)']
        self.sat_fat = macros['FATTY ACIDS, SATURATED, TOTAL']
        self.fiber = macros['FIBRE, TOTAL DIETARY']
        self.carbs = macros['CARBOHYDRATE, TOTAL (BY DIFFERENCE)']

    def change_serving(self, factor):
        self.calories = self.calories * factor
        self.proteins = self.proteins * factor
        self.fat = self.fat * factor
        self.sat_fat = self.sat_fat * factor
        self.fiber = self.fiber * factor
        self.carbs = self.carbs * factor

class Food:
    def __init__(self, food_name, selected_measure, calories, proteins,
                 fat, sat_fat, fiber, carbs):
        self.food_name = food_name
        self.measures = ''
        self.selected_measure = selected_measure
        self.calories = calories
        self.proteins = proteins
        self.fat = fat
        self.sat_fat = sat_fat
        self.fiber = fiber
        self.carbs = carbs

    def load_measure(self, result_set):
        self.measures = [res[2] for res in result_set]

    def load_macros(self, result_set):
        macros = {}

        for res in result_set:
            value = round(res[4], 2)
            macros[res[3]] = value

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

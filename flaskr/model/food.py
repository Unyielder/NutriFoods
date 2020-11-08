class Food:
    def __init__(self, food_name, measure, unit, calories, proteins,
                 fat, sat_fat, fiber, carbs):
        self.food_name = food_name
        self.measure = measure
        self.unit = unit
        self.calories = calories
        self.proteins = proteins
        self.fat = fat
        self.sat_fat = sat_fat
        self.fiber = fiber
        self.carbs = carbs

    def change_serving(self, factor):
        self.measure = self.measure * factor
        self.calories = self.calories * factor
        self.proteins = self.proteins * factor
        self.fat = self.fat * factor
        self.sat_fat = self.sat_fat * factor
        self.fiber = self.fiber * factor
        self.carbs = self.carbs * factor



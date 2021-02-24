from collections import defaultdict


class Food:
    def __init__(self):
        self.id = None
        self.name = ''
        self.measure = ''
        # Macros
        self.calories = None
        self.proteins = None
        self.fat = None
        self.sat_fat = None
        self.fiber = None
        self.carbs = None
        # Vitamins
        self.alpha_tocopherol_added = None
        self.alpha_tocopherol = None
        self.beta_tocopherol = None
        self.gamma_tocopherol = None
        self.delta_tocopherol = None
        self.folate = None
        self.pantothenic_acid = None
        self.thiamin = None
        self.biotin = None
        self.vitamin_b12 = None
        self.vitamin_b12_added = None
        self.vitamin_b6 = None
        self.total_niacin = None
        self.niacin_preformed = None
        self.folacin = None
        self.folate = None
        self.folic_acid = None
        self.riboflavin = None
        self.vitamin_c = None
        self.vitamin_d2_d3 = None
        self.vitamin_d = None
        self.vitamin_d2 = None
        self.vitamin_k = None
        self.retinol = None
        self.retinol_activity_equi = None
        self.alpha_carotene = None
        # Minerals
        self.zinc = None
        self.selenium = None
        self.calcium = None
        self.potassium = None
        self.iron = None
        self.manganese = None
        self.magnesium = None
        self.copper = None

    def load_measure(self, result_set):
        self.measure = [res[2] for res in result_set]

    def load_macros(self, result_set):
        macros = defaultdict(list)

        self.id = result_set[0][0]
        self.name = result_set[0][1]
        self.measure = result_set[0][2]

        for res in result_set:
            macros[res[3]].append(res[4])
            macros[res[3]].append(res[5])

        self.calories = macros['ENERGY (KILOCALORIES)']
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

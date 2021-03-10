from collections import defaultdict


class Food:
    def __init__(self):
        self.id = None
        self.name = ''
        self.measure = ''

        # Macros
        self.calories = None
        self.carbs = None
        self.fat = None
        self.sat_fat = None
        self.proteins = None
        self.fiber = None
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
        self.beta_carotene = None
        # Minerals
        self.zinc = None
        self.selenium = None
        self.calcium = None
        self.potassium = None
        self.iron = None
        self.manganese = None
        self.magnesium = None
        self.copper = None
        # Amino-acids
        self.valine = None
        self.tyrosine = None
        self.tryptophan = None
        self.threonine = None
        self.theobromine = None
        self.proline = None
        self.serine = None
        self.phenylalamine = None
        self.alanine = None
        self.aspartic_acid = None
        self.aspartame = None
        self.leucine = None
        self.lysine = None
        self.isoleucine = None
        self.hydroxyproline = None
        self.histidine = None
        self.glycine = None
        self.glutamic_acid = None
        self.methionine = None
        self.cystine = None
        self.arginine = None
        # Surgars
        self.surgars_total = None
        self.lactose = None
        self.glucose = None
        self.galactose = None
        self.sucrose = None
        self.fructose = None
        self.maltose = None
        self.mannitol = None
        self.monosaccharides_total = None
        self.disaccharides_total = None
        self.sorbitol = None
        # Steroids
        self.campesterol = None
        self.stigmasterol = None
        self.beta_sitosterol = None
        self.total_plant_sterol = None
        self.cholesterol = None
        # Misc
        self.phosphorus = None
        self.oxalic_acid = None
        self.moisture = None
        self.lycopene = None
        self.luteine_and_zeaxanthine = None
        self.choline_total = None
        self.caffeine = None
        self.betaine = None
        self.beta_cryptoxanthin = None
        self.ash_total = None
        self.alcohol = None

    def load_measure(self, result_set):
        self.measure = [res[2] for res in result_set]

    def load_nutrients(self, result_set):
        macros = defaultdict(list)

        for res in result_set:
            macros[res[3]].append(res[4])
            macros[res[3]].append(res[5])

        # Macros
        self.calories = macros['ENERGY (KILOCALORIES)']
        self.proteins = macros['PROTEIN']
        self.fat = macros['FAT (TOTAL LIPIDS)']
        self.sat_fat = macros['FATTY ACIDS, SATURATED, TOTAL']
        self.fiber = macros['FIBRE, TOTAL DIETARY']
        self.carbs = macros['CARBOHYDRATE, TOTAL (BY DIFFERENCE)']

        # Vitamins
        self.alpha_carotene = macros['ALPHA CAROTENE']
        self.beta_carotene = macros['BETA CAROTENE']
        self.retinol = macros['RETINOL']
        self.vitamin_d = macros['VITAMIN D (INTERNATIONAL UNITS)']
        self.vitamin_d2 = macros['VITAMIN D2, ERGOCALCIFEROL']
        self.d2_d3 = macros['VITAMIN D (D2 + D3)']
        self.vitamin_c = macros['VITAMIN C']
        self.thiamine = macros['THIAMIN']
        self.riboflavin = macros['RIBOFLAVIN']
        self.niacin_preformed = macros['NIACIN (NICOTINIC ACID) PREFORMED']
        self.total_niacin = macros['TOTAL NIACIN EQUIVALENT']
        self.vitamin_b6 = macros['VITAMIN B-6']
        self.folacin = macros['TOTAL FOLACIN']
        self.vitamin_b12 = macros['VITAMIN B-12']
        self.vitamin_b12_added = macros['VITAMIN B12, ADDED']
        self.folic_acid = macros['FOLIC ACID']
        self.folate = macros['NATURALLY OCCURRING FOLATE']
        self.retinol_activity_equi = macros['RETINOL ACTIVITY EQUIVALENTS']
        self.alpha_tocopherol = macros['ALPHA-TOCOPHEROL']
        self.alpha_tocopherol_added = macros['ALPHA-TOCOPHEROL, ADDED']
        self.beta_tocopherol = macros['BETA-TOCOPHEROL']
        self.gamma_tocopherol = macros['GAMMA-TOCOPHEROL']
        self.delta_tocopherol = macros['DELTA-TOCOPHEROL']
        self.pantothenic_acid = macros['PANTOTHENIC ACID']
        self.vitamin_k = macros['VITAMIN K']
        self.biotin = macros['BIOTIN']

        # Minerals
        self.zinc = macros['ZINC']
        self.selenium = macros['SELENIUM']
        self.calcium = macros['CALCIUM']
        self.potassium = macros['POTASSIUM']
        self.iron = macros['IRON']
        self.manganese = macros['MANGANESE']
        self.magnesium = macros['MAGNESIUM']
        self.copper = macros['COPPER']

        # Amino-acids
        self.valine = macros['VALINE']
        self.tyrosine = macros['TYROSINE']
        self.tryptophan = macros['TRYPTOPHAN']
        self.threonine = macros['THREONINE']
        self.theobromine = macros['THEOBROMINE']
        self.proline = macros['PROLINE']
        self.serine = macros['SERINE']
        self.phenylalamine = macros['PHENYLALANINE']
        self.alanine = macros['ALANINE']
        self.aspartic_acid = macros['ASPARTIC ACID']
        self.aspartame = macros['ASPARTAME']
        self.leucine = macros['LEUCINE']
        self.lysine = macros['LYSINE']
        self.isoleucine = macros['ISOLEUCINE']
        self.hydroxyproline = macros['HYDROXYPROLINE']
        self.histidine = macros['HISTIDINE']
        self.glycine = macros['GLYCINE']
        self.glutamic_acid = macros['GLUTAMIC ACID']
        self.methionine = macros['METHIONINE']
        self.cystine = macros['CYSTINE']
        self.arginine = macros['ARGININE']

        # Surgars
        self.surgars_total = macros['SUGARS, TOTAL']
        self.lactose = macros['LACTOSE']
        self.glucose = macros['GLUCOSE']
        self.galactose = macros['GALACTOSE']
        self.sucrose = macros['SUCROSE']
        self.fructose = macros['FRUCTOSE']
        self.maltose = macros['MALTOSE']
        self.mannitol = macros['MANNITOL']
        self.monosaccharides_total = macros['TOTAL MONOSACCARIDES']
        self.disaccharides_total = macros['TOTAL DISACCHARIDES']
        self.sorbitol = macros['SORBITOL']

        # Steroids
        self.campesterol = macros['CAMPESTEROL']
        self.stigmasterol = macros['STIGMASTEROL']
        self.beta_sitosterol = macros['BETA-SITOSTEROL']
        self.total_plant_sterol = macros['TOTAL PLANT STEROL']
        self.cholesterol = macros['CHOLESTEROL']

        # Misc
        self.phosphorus = macros['PHOSPHORUS']
        self.oxalic_acid = macros['OXALIC ACID']
        self.moisture = macros['MOISTURE']
        self.lycopene = macros['LYCOPENE']
        self.luteine_and_zeaxanthine = macros['LUTEIN AND ZEAXANTHIN']
        self.choline_total = macros['CHOLINE, TOTAL']
        self.caffeine = macros['CAFFEINE']
        self.betaine = macros['BETAINE']
        self.beta_cryptoxanthin = macros['BETA CRYPTOXANTHIN']
        self.ash_total = macros['ASH, TOTAL']
        self.alcohol = macros['ALCOHOL']

    def change_serving(self, factor):
        for attr, value in self.__dict__.items():
            if type(value) == list:
                value = value * factor
                self.__dict__[attr] = value

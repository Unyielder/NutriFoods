class Queries:
    def __init__(self, var):
        self.var = var
        self.measure = ''
        self.ingredient_query = f"""
            SELECT FoodID, FoodDescription
            FROM FOOD_NAME
            WHERE FoodDescription LIKE '{self.var}%'       
        """
        self.measures_query = f"""
            SELECT DISTINCT
            fn.FoodID, 
            fn.FoodDescription, 
            mn.MeasureDescription
            FROM FOOD_NAME fn
            LEFT JOIN CONVERSION_FACTOR cf ON
	            fn.FoodID = cf.FoodID
            LEFT JOIN MEASURE_NAME mn ON 
	            cf.MeasureID = mn.MeasureID
            WHERE fn.FoodID = {self.var}
        """
        self.macro_query = f"""
            SELECT 
            fn.FoodID, fn.FoodDescription, 
            mn.MeasureDescription, nn.NutrientName, 
            cf.ConversionFactorValue * na.NutrientValue AS "NutrientValCalc",
            nn.NutrientUnit
            FROM FOOD_NAME fn
            LEFT JOIN CONVERSION_FACTOR cf ON
            	fn.FoodID = cf.FoodID
            LEFT JOIN MEASURE_NAME mn ON 
	            cf.MeasureID = mn.MeasureID
            LEFT JOIN NUTRIENT_AMOUNT na ON 
	            fn.FoodID = na.FoodID
            LEFT JOIN NUTRIENT_NAME nn ON
	            na.NutrientID = nn.NutrientID
            WHERE nn.NutrientCode IN (208, 203, 204, 606, 291, 205)
            AND fn.FoodID = {self.var}
            AND mn.MeasureDescription = {self.measure}
        """

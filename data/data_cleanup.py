import pandas as pd
from sqlalchemy import create_engine

# Conveting all csv files into dataframes
food_name = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/FOOD NAME.csv", encoding='latin-1')
food_group = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/FOOD GROUP.csv", encoding='latin-1')
conversion_factor = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/CONVERSION FACTOR.csv", encoding='latin-1')
food_source = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/FOOD SOURCE.csv", encoding='latin-1')
measure_name = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/MEASURE NAME.csv", encoding='latin-1')
nutrient_amount = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/NUTRIENT AMOUNT.csv", encoding='latin-1')
nutrient_name = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/NUTRIENT NAME.csv", encoding='latin-1')
nutrient_source = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/NUTRIENT SOURCE.csv", encoding='latin-1')
yield_amount = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/YIELD AMOUNT.csv", encoding='latin-1')
yield_name = pd.read_csv(r"C:\Users\Mohamed\Documents\Datasets\Canadian Nutrient File/YIELD NAME.csv", encoding='latin-1')

# Data has already been cleaned by public workers, simply dropping columns that aren't needed
food_name = food_name.drop(['FoodDateOfPublication', 'CountryCode', 'ScientificName', 'FoodDescriptionF'], axis=1)
food_group = food_group.drop(['FoodGroupNameF'], axis=1)
food_source = food_source.drop(['FoodSourceDescriptionF', 'Unnamed: 4', 'Unnamed: 5'], axis=1)
measure_name = measure_name.drop(['MeasureDescriptionF', 'Unnamed: 3', 'Unnamed: 4'], axis=1)
nutrient_amount = nutrient_amount.drop(['StandardError', 'NumberofObservations'], axis=1)
nutrient_name = nutrient_name.drop(['NutrientNameF'], axis=1)
nutrient_source = nutrient_source.drop(['NutrientSourc DescriptionF'], axis=1)
yield_amount = yield_amount.drop(['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7'], axis=1)
yield_name = yield_name.drop(['YieldDescriptionF'], axis=1)

# Creating database
engine = create_engine('sqlite:///Canadian_Foods.db')

# Creating database tables with these dataframes
users = pd.DataFrame({'id': [], 'UserName': [], 'PassWord': []})

users.to_sql('USERS', con=engine, index=False)
food_name.to_sql('FOOD_NAME', con=engine, index=False)
food_group.to_sql('FOOD_GROUP', con=engine, index=False)
conversion_factor.to_sql('CONVERSION_FACTOR', con=engine, index=False)
food_source.to_sql('FOOD_SOURCE', con=engine, index=False)
measure_name.to_sql('MEASURE_NAME', con=engine, index=False)
nutrient_amount.to_sql('NUTRIENT_AMOUNT', con=engine, index=False)
nutrient_name.to_sql('NUTRIENT_NAME', con=engine, index=False)
nutrient_source.to_sql('NUTRIENT_SOURCE', con=engine, index=False)
yield_amount.to_sql('YIELD_AMOUNT', con=engine, index=False)
yield_name.to_sql('YEILD_NAME', con=engine, index=False)
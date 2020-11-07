import pandas as pd
import re

pd.set_option('display.max_rows', 500)
file = r"C:\Users\Mohamed\Documents\Datasets\food_nutrients.csv"


def clean_data(csv):
    pattern = "\s.*"
    new_measures = []
    units = []

    data = pd.read_csv(csv)
    for row in data['Measure']:
        match = re.findall(pattern, row)
        print(match)
        new_measures.append(row.replace(match[0], ''))
        units.append(match[0])

    data['Measure'] = new_measures
    data['Units'] = units
    return data


df = pd.read_csv(file)

print(df[['Food', 'Measure']])


# df = clean_data(file)
# print(df)
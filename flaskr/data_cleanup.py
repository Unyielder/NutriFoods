import sqlite3
import pandas as pd
import re

pd.set_option('display.max_rows', 500)
DATABASE = r"../instance/flaskr.sqlite"
con = sqlite3.connect(DATABASE)
sql = "SELECT * FROM MEASURE_NAME"

df = pd.read_sql(sql, con)

print(df)



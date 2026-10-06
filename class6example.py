from pathlib import Path

import pandas as pd

data_path = Path("data") / "messy_netflix_titles.csv"
df = pd.read_csv(data_path)



print(df.shape) 
print(df.head())
print(df.columns) 
print(df.dtypes) 
df.info() 
print(df.describe())

recent = df[df["release_year"] >= 2020]
print(recent)
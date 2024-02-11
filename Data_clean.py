import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/meteorite-landings/Meteorite_Landings.csv")
df.head()

df = df[['year','mass']]

def clean(x):
    year = x.split("")[0]
    return year 
df['year'] = df['year'].apply(clean) 

df.sort_values(by='year')

df.to_csv('clean_meteorite_landings.csv', index = False)

Print(df)

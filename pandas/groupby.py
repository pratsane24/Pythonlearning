# Questions:- 1. Find Max temp in each cities
# 2. Find average windspeed per city
# In this we will group the data and then do the analytics

import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv("cityweather.csv")
# print(df)
# import pandas as pd

# Grouping of column according to city

df = pd.read_csv("cityweather.csv")
# print("Columns in DataFrame:", df.columns)  # Check column names
# print(df)
# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Group by 'city' after ensuring the column name is correct
g = df.groupby("city")
print(g)

# Printing groups of data
# for city, city_df in g:
#     print(city)
#     print(city_df)

# IF u want specific data group then
# print(g.get_group("mumbai"))

# MAx temp of each city
# print(g.max())
# OR ALTERNATE METHOD
# print(g['temp'].max())n 

# average windspeed in each city
# print(g.mean()) , This is giving error
# print(g['windspeed'].mean())

# If u want to get analytics in one shot then use
# print(g.describe()) 


# Matplotlib
# %matplotlib inline
print(g.plot())
print(plt.show())

# How to handle missing data?
# 1.Fill na to fill missing values usuing different ways
# 2.interpolate to make a guess on missing values using interpolation
# 3.drop na to drop rows with missing values

# import pandas as pd
# df = pd.read_csv("missingdata.csv")
# print(df)

# Want to change date format
# df = pd.read_csv("missingdata.csv",parse_dates=["date"])
# print(type(df.date[0]))
# print(df)

# use date as index in dataframe
# df = pd.read_csv("missingdata.csv",parse_dates=["date"])
# df.set_index('date',inplace=True)
# print(df)

# USE FILL NA
# new_df = df.fillna(0)
# print(new_df)

# In event also there is blank space what is the use of zero there,
# We can use dictonary in that case
# new_df = df.fillna({
#     'temp':0,
#     'windspeed':0,
#     'event':'no event'
# })
# print(new_df)

# Getting better estimate
# new_df = df.bfill()
# print(new_df)

# # Axis parameter
# In this method it is copying value from column, previously it was taking values from 
# previous row but now in this it is taking values from column
# new_df =df.fillna(method="bfill", axis= "columns")
# print(new_df)

# Limit
# In limit if u r filling values in forward fill, n there are 2 empty rows from which u just need to fill value in 
# just one row, then limit comes into function.
# new_df =df.fillna(method="ffill", limit=1)
# print(new_df)

# Interpolate
# e.g in temp one day is 32 and other day's temp is missing so we need to interpolate it bze
# the next temp is less there cannot be sudden drop in temp to a greater extend.
# new_df =df.interpolate()
# print(new_df)

# Time
# In this interpolation we have considered the data, but not time
# Lets see there is data missing for month of feb n march
# So if we consider time then it will give different interpolation data for april.

# new_df =df.interpolate(method="time")
# print(new_df)

# Dropna
# In this whichever row has NaN value, we it drop it
# It will print only rows that rows which has valid values.
# new_df =df.dropna()
# print(new_df)

# IF u want to drop rows which has all parameters as NaN.
# new_df =df.dropna(how="all")
# print(new_df)

# IF u wanna go by non NaN values then?
# thresh=1 means If we have aleast 1 non-NaN value then print that row.
# Here we does not consider date as it is the index value.
# new_df =df.dropna(thresh=1)
# print(new_df)

# How we go insert missing dates?
# We create date range
# dt = pd.date_range("01-01-2017","01-11-2017")
# idx = pd.DatetimeIndex(dt)
# df = df.reindex(idx)
# print(df)

import pandas as pd
import numpy as np
# df = pd.read_csv("missingdata1.csv")
# print(df)

# new_df = df.replace(-99999,np.nan)
# print(new_df)

# What if there are 2 spl values
# new_df = df.replace([-99999,88888], np.nan)
# print(new_df)

# THere is no event in event column which is also need to be replaces but we cannot replace it 
# by above method since the value which is invalid for 1 column can be valid for other column
# We need to replace value based on specific column
# by providing dictonary

# new_df = df.replace({
#     'temp': -99999,
#     'windspeed': -99999,
#     'event':'No Event'
# },np.nan)
# print(new_df)

# If there is any No event in event and u want to replace it by Sunny then just use mapping.
# new_df = df.replace({
#     -99999:np.nan,
#     'No Event':'Sunny'
# })
# print(new_df)

# If there is unit added to the temp n windspeed and now u want to replace it with blank space or chop it off.
# Then easy way is to use regex (regular expression)
# They are use to replace pattern
# new_df = df.replace({
#     'temp':'[A-Za-z]',
#     'windspeed':'[A-Za-z]'
# },'',regex=True)
# print(new_df)

# How u can replace a list of values with another list of values
df = pd.DataFrame({
    'score':['exceptional','average','good','poor','average','exceptional'],
    'student':['rob','maya','parthvi','tom','julian','erica']
})
print(df)

# In this score must be in numbers but it is in words.
# Here we can do mapping internally means poor means zero(0).
# Now  we want to replace words with number then we have to do
new_df = df.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(new_df)


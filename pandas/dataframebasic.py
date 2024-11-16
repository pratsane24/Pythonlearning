import pandas as pd
df = pd.read_csv("dataframe.csv")
# print(df)
# NOTE:- in this save excel file as .csv and not .xlxs if you want to import the excel file in python pandas.
# and use csv(macintosh) type from dropdown.
# print(df)
# print(df[2:5])
# print(df.columns)
# print(df.temperature)
# print(df.windspeed)
# print(df.date)
# print(df.event)
# another method to write same thing.
# print(df["event"])
# print(type(df["event"]))
# print(df[['event','date','temperature']])
# NOTE:- there should be use of ' ' single quote and double square brackets [[]] always to get output.

# OPERATIONS IN DATAFRAME
# Question :- maximum temperature?
# print(df['temperature'].max())

# Question :- average temperature?
# print(df['temperature'].mean())

# Question:- Describe the details or statistics
# print(df.describe())

# Question:- rows/data which give temp>32
# print(df[df.temperature>=32])

# Question:- rows/data When temp was max
# print(df[df.temperature==df.temperature.max()])

# IF u don't want to print the enitire row, just want to print date then 
# print(df['date'][df.temperature==df.temperature.max()])

# IF u don't want to print the enitire row, just want to print date then temperature
# NOTE:- here use double square brackets [[]], for date n temperature.
# print(df[['date','temperature']][df.temperature==df.temperature.max()])

# print(df.index)

# If u want to remove index value than use 
# print(df.set_index('date'))

# If you are doing any changes in df it is not replacing the original df, It remains same.
# So if u want to replace df with new values(modify the original one) then use the following code.
# df.set_index('date',inplace =True)
# print(df)

# print(df.loc['01 January 2017']) getting error.

# IF u want to reset ur original df then use
df.reset_index(inplace=True)
print(df)
print(df.set_index('event'))

# print(df[df['event'] == 'Snow'])

# print(df.loc['Rain']) - getting error.


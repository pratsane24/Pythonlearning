# import pandas as pd
# df = pd.read_csv("stockdata.csv")
# print(df)

# NOTE:- If u have to skip or delete a row from reading then us can use the following method.
# df = pd.read_csv("stockdata.csv",skiprows=1)
# print(df)

# ANother way
# df = pd.read_csv("stockdata.csv",header=1)
# print(df)

# NOTE:- index starts from 0 hence header=1 really means row #2 in csv file.

# Lets consider csv file which doesn't have header then?
# df = pd.read_csv("stockdata.csv",header=None)
# print(df)

# Now if u want to provide names to header than use
# df = pd.read_csv("stockdata.csv",header=None, names=["tickers","eps","revenue","price","people"])
# print(df)

# Now if u want to read only read 3 rows from dataframe then
# df = pd.read_csv("stockdata.csv", nrows=3)
# print(df)

# There are many values which are not available or n.a in dataframe then it will get  replaced by NaN?
# This is usefull to clean ur messy csv or excel data.
# df = pd.read_csv("stockdata.csv", na_values=["not available","n.a."])
# print(df)

# In this file, there is -1 as revenue i.e revenue of any company cannot be zero, it can 0 or more than zero.
# so u want to convert it into NaN but the problem is -1 in eps will also get converted into NaN if u add command in the df value
# But eps can be negative so then u can use dictonary.

# df = pd.read_csv("stockdata.csv", na_values={
#     'eps': ["not available","n.a."],
#     'revenue' : ["not available","n.a.",-1],
#     'price' : ["not available","n.a."],
#     'people' : ["not available","n.a."]
# })
# print(df)

# Now this was read csv now how about writing back to csv?
# df.to_csv('new.csv')
# In this it by default writes he index , if u don't want it write it as index=false.
# df.to_csv('new.csv',index=False)

# Sometimes u don't want to print all the arrugements, for e.g u just need to get only to 2 columns tickers and eps & I 
# want skip exporting remaining 3 coluns to my csv file then use
# print(df.columns)
# df.to_csv('new.csv',header=False,columns=['tickers','eps'])

# NOW LETS SEE HOW TO READ AND WRITE IN EXCEL

# import pandas as pd
# df = pd.read_excel("stockdata.xlsx","Sheet1")
# print(df)

# Sometimes u want to do conversion of ur cell content from excel e.g WMT people is n.a. and u its was Sam Walton,
# then u want convert it into Sam Wakton then u use convert ?
# if u want to do convesion into eps column the?

# def convert_people_cell(cell):
#     if cell =="n.a.":
#         return 'sam walton'
#     return cell

# def convert_people_cell(cell):
#     if cell =="not available":
#         return None
#     return cell

# df = pd.read_excel("stockdata.xlsx","Sheet1",converters={
#     'people': convert_people_cell,
#     'eps': convert_people_cell
# })
# print(df)

# Now if u want write it back to excel then
# df.to_excel("new1.xlsx",sheet_name="stocks")

# If u want to start ur table from row=1 & col=2 then?
# df.to_excel("new1.xlsx",sheet_name="stocks",startrow=1,startcol=2)

# If u want to skip index then?
# df.to_excel("new1.xlsx",sheet_name="stocks",startrow=1,startcol=2,index=False)



# IF u have 2 dataframe and want to share it in two different sheets in one excel file?

# Now we will create 2 different dataframe

import pandas as pd

df_stocks = pd.DataFrame({
    'tickers':['GOOGLE','WMT','MSFT'],
    'pe':[30.37,14.26,30.97],
    'eps':[27.82,4.61,2.12]
})

df_weather = pd.DataFrame({
    'date' : ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature':[32,35,28],
    'event': ['Rain','Sunny','Snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
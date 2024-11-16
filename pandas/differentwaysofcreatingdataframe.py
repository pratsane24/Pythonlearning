import pandas as pd

# # NOTE:- USING CSV
# df = pd.read_csv("dataframe.csv")
# print(df)

# # NOTE:-USING EXCEL
# df = pd.read_excel("dataframe.xlsx","dataframe")
# print(df)

# # NOTE:- USING PYTHON DICTIONARY
# dataframe = {
#     'date':['1/1/2017','1/2/2017','1/3/2017'],
#     'temperature':[32,35,28],
#     'windspeed' :[6,7,2],
#     'event' :['Rain','Snow','Sunny']
# }
# df = pd.DataFrame(dataframe)
# print(df)

# # NOTE:- USING LIST OF TUPLE
# dataframe = [
#     ('1/1/2017',32,6,'Rain'),
#     ('1/2/2017',35,7,'Sunny'),
#     ('1/3/2017',28,2,'Snow')
# ]
# df = pd.DataFrame(dataframe,columns=["date","temperature","windspeed","event"])
# print(df)

# # NOTE:- BY USING DICTIONARIES
# dataframe = [
#             {'date' : '1/1/2017','temperature' : 32,'windspeed':6,'event':'Rain'},
#             {'date' : '1/2/2017','temperature' : 35,'windspeed':7,'event':'Sunny'},
#             {'date' : '1/3/2017','temperature' : 28,'windspeed':2,'event':'Snow'},
# ]
# df = pd.DataFrame(dataframe)
# print(df)

# import pandas as pd
# import matplotlib as plt
# df = pd.read_csv("pandas/apple.csv")
# print(df.head())
# # Now we need to generate date bze it looks boring without dates 

# rng = pd.date_range(start="6/1/2016",end="5/17/2017",freq='B')
# print(rng)
# # here B means bussiness days

# df.set_index(rng,inplace=True)
# print(df)


# NOTE :- BELOW CODE IS OBTAINED FROM CHATGPT AND THIS GIVES OUTPUT.



import pandas as pd
import matplotlib.pyplot as plt

# Read data and create date range
df = pd.read_csv("pandas/apple.csv")
rng = pd.date_range(start="6/1/2016", end="5/17/2017", freq="B")
df.set_index(rng, inplace=True)

# Plot the Close column
# df['Close'].plot()
# plt.title("Stock Close Prices Over Time")
# plt.xlabel("Date")
# plt.ylabel("Close Price")
# plt.show()

# HOW TO GET PARTIAL DF?
print(df["2017-06-01":"2017-06-10"].Close.mean())


# NOTE : I HAVE TO PUSH THIS FILE TO GIT SINCE THERE ARE LOTS OF ERROR, I NEED TO SORT ALL ERROR N THEN 
# PUSH IT.
# Queston:- Home prices in Monroe Twp,NJ(USA)
# Area      prices
# 2600      550000
# 3000      565000
# 3200      610000
# 3600      680000
# 4000      725000
# Given these home prices find out prices of homes whose area is,
# (i)3300 Sq.ft
# (ii)5000 Sq.ft

# Solution
# NOTE:-   
# In this, we are using graph eqn
# y = mx + c 
# where m = slope(or Gradient)
# c = Y - intercept
# similary, price = m * area + b
# where, area = Independent variable
# price = Dependent variable

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model 

df = pd.read_csv("machinelearning/homeprices.csv")
# print(df)

# %matplotlib inline
# print(plt.xlabel("Area(sq.ft)"))
# print(plt.ylabel("Prices(US$)"))
# print(plt.scatter(df.Area,df.Prices, color="red",marker="*"))


# NOTE :- ALWAYS USE "print(plt.show())" AT GTHE END OF THE CODE WHILE YOU ARE USING MATPLOTLIB IN YOUR CODE.

reg = linear_model.LinearRegression()
print(reg.fit(df[['Area']],df.Prices))


# NOTE :- If the terminal is hanging after plt.show(), check whether the plot window is still open.
# Close the plot window manually to allow the script to finish and return to the terminal prompt.
# SO AFTER GETTING YOUR OUTPUT, CLOSE GRAPH WINDOW THEN ONLY THE CODE WILL GET TERMINATED.

# # NOTE :- NOW WE CAN PREDIT PRICES FOR ANY AREA.
# # Predict for a new value (3300 sq.ft)
# prediction = reg.predict([[3300]]) 
#  # Pass the value as a 2D array
# print(f"Predicted price for 3300 sq.ft: {prediction[0]}")
# # print(reg.predict(3300))

# NOTE:- ALWAY PRINT plt.show() at the end of code.

# m = reg.coef_
# print("Coef :- ",m)
# c = reg.intercept_
# print("Intercept(c) :- ",c)
# NOTE :- JUST A TRIAL AND ERROR
# area = print(input("please enter the area to be predicted"))
# # y = mx+c
# # x = area to be predicted
# # y = price of area
# # m = coef
# # c = intercept
# y = m * area + c
# print( "Price of area =",y)
# NOTE:- Here u have entered the area manually.
# print(3300* m + c)
# print(plt.show())

# NOW YOU WANT TO CALCULATE FOR 5000 THEN JUST REPLACE 3300 BY 5000.

# prediction = reg.predict([[5000]]) 
#  # Pass the value as a 2D array
# print(f"Predicted price for 5000 sq.ft: {prediction[0]}")
# # print(reg.predict(5000))
# m = reg.coef_
# print("Coef :- ",m)
# c = reg.intercept_
# print("Intercept(c) :- ",c)
# print(5000* m + c)
# print(plt.show())


# NOTE :- NOW I HAVE A LIST OF AREAS AVAILABLE IN CSV FILE, 
# d = pd.read_csv("machinelearning/area.csv")
# print(d.head(3))
# p = reg.predict(d)
# d['Prices'] = p
# # print(d)
# d.to_csv("machinelearning/areaprices.csv",index=False)

# NOW LET'S GO TO OUR ORIGINAL QUESTION
print(plt.xlabel("Area(sq.ft)", fontsize = 20))
print(plt.ylabel("Prices(US$)", fontsize = 20))
print(plt.scatter(df.Area,df.Prices, color="red",marker="*"))
print(plt.plot(df.Area,reg.predict(df[['Area']]),color = "blue"))
print(plt.show())


# THis is from lec no 5. Save Model Using Joblib and pickle
# Ask question to this below module and u will get the soln.

# import pickle
# with open ('model_pickle','wb') as f:
#     pickle.dump(model,f)
# with open ('model_pickle','rb') as f:
#      mp  = pickle.load(f)

# # for JOBLIB
# from sklearn.externals import joblib
# joblib.dump(model,'machinelearning/model_joblib')
# # OUTPUT :- ['model_joblib']
# mj = joblib.load('machinelearning/model_joblib')
# print(mj.predict(5000))

#  NOTE:- Lots of Error in this lec.
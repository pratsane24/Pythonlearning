# Question:- Givrn those home prices find out price of aa home that has,
# 3000 sqr.ft area,3 bedrooms, 40 yrs old
# 2500 sqr.ft area,4 bedrooms, 5 years old.

# MATHEMATICAL EQN
# price = m1*area + m2*bedrooms + m3*age + b
# here price is dependent variablr
# area,bedrooms,age is independent variable(features)
# m1,m2,m3 is called coefficent
# b is intercept
# i.e y = m1x1 + m2x2 + m3x3 + b
# Topic to be covered are
# data Pre-processing : HAndling NA values
# Linear Regression USing Multiple Variables


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model 

df = pd.read_csv("machinelearning/multiple.csv")
# print(df)

# Calculate median since no of bedrrom is missing
import math
median_bedrooms = math.floor(df.bedrooms.median())
# print(median_bedrooms)

# fillna() with median value 
# print(df.bedrooms.fillna(median_bedrooms))

# Now we need to fill the series so that we can update it to our original df.
df.bedrooms = df.bedrooms.fillna(median_bedrooms)
# print(df)

reg = linear_model.LinearRegression()
# fit() method is use to train your model.
reg.fit(df[['area','bedrooms','age']],df.price)
print(reg.fit(df[['area','bedrooms','age']],df.price))

# print(reg.coef_)
# print(reg.intercept_)
# print(reg.predict([[3000,3,40]]))
print(reg.predict([[2500,4,5]]))

# Wanna do it actually substituting the value
# a= 137.25*3000+(-26025*3)+(-6825*40)+383724.99999
# print(a)

# b= 137.25*2500+(-26025*4)+(-6825*5)+383724.99999
# print(b)
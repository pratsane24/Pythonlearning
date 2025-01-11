# In this we will use 80% data to train the model while 20% to test the model.
# In this Mileage and Age are independent variable while selling price is dependent variable.

import pandas as pd
df = pd.read_csv("machinelearning/carprices.csv")
# print(df.head())

import matplotlib.pyplot as plt
# %matplotlib inline
# print(plt.scatter(df['Mileage'],df['Sell Price($)']))
# print(df.plot()) This will give output for all the 3 variables.
# print(plt.scatter(df['Age(yrs)'],df['Sell Price($)']))
# print(plt.show())

# Now we will linear regression model based on this visualization

X = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']
# print(X)
# print(y)

from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
# NOTE:- 0.2 is 20% of total to be tested
# print(len(X_train))
# When you print X_train everytime you will get different output.
# Since it is set of samples used for training.
# And sometimes u want to use same set of sample then use this function Random state method.
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=10)
# print(len(X_train))
# print(X_train)
# print(len(X_test))
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
print(clf.fit(X_train,y_train))
print(clf.predict(X_test))
print(y_test)
print(clf.score(X_test,y_test))
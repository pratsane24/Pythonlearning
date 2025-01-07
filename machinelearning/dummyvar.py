import pandas as pd
df = pd.read_csv("machinelearning/houseprices.csv")
# print(df)
dummies = pd.get_dummies(df.town ,dtype=int)
# print(dummies)
merged = pd.concat([df,dummies],axis = 'columns')  
# print(merged)        

# NOTE: For dummy variable there is 1 rule, if u have 4 dummpy variable u will have to drop 1 dummy variable.
# In this we have 3 nos of dummy variable u will have to drop 1.
# We can select any of them, In this E.g I am going to drop wet windsor.

final = merged.drop(['town','west windsor'],axis='columns')
# print(final)
# Now here in output dataset looks good all the numerical values and 1 dummy varicble is also dropped.
# NOTE :- when u use sk learn linear regression model it will work even if you don't drop it bze linear regression model is aware about dummpy 
# variable trap & it will drop automatically, but in general it is good practice that u drop it on your own.

# NOw let's create linear regression  model.

from sklearn.linear_model import LinearRegression
model = LinearRegression()
# Now u need to give x & y, there accept price everythng is x. since price is dependent variable.
# Now drop price from X column

X = final.drop('price',axis ='columns')
# print(X)
y = final.price
# print(y)
# print(model.fit(X,y))
# print(model.predict([[2800,0,1]]))
# print(model.predict([[3400,0,0]]))
# print(model.score(X,y))

# ONE HOT ENCODING, 1st you need to do label encoding sql & pre-processing & create the label encoder class object
# Class object is ready & then use that on our original data frame so we call it df.

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dfle = df
dfle.town = le.fit_transform(dfle.town)
# print(dfle)

X = df[['town','area']].values
# print(X)
y = dfle.price
print(y)
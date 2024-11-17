import pandas as pd
# df1 = pd.DataFrame({
#     "city":["New york","Chicago","Orlando"],
#     "Temp":[21,14,35]
# })
# # print(df1)

# df2 = pd.DataFrame({
#     "city":["Chicago","New york","Orlando"],
#     "Humadity":[65,68,75]
# })
# # print(df2)

# # If u want to merge df1 and df2?
# # It is same as database join
# df3 = pd.merge(df1,df2,on="city")
# print(df3)

# IF u have different cities?
# df1 = pd.DataFrame({
#     "city":["New york","Chicago","Orlando","baltimore"],
#     "Temp":[21,14,35,32]
# })
# # print(df1)

# df2 = pd.DataFrame({
#     "city":["Chicago","New york","San Francisco"],
#     "Humadity":[65,68,75]
# })
# print(df2)
# df3 = pd.merge(df1,df2,on="city")
# print(df3)
# here in this result, it will only give 2 cities which are common in both.
# it is missing the other cities which are not in common bze it works on principle of set intersection.
# it will only give the intersection part
# Also in database wall there is a conceptof inner join which is same as intersection.
# 2nd join in database is outer join,if u will be looking by set theory than it is Union of 2 set.
# So fot that case use follow code/way/method.
# How will ask u what u want like outer join, left join,right join,etc.
# Df1 is right n df2 is left.
# df3 = pd.merge(df1,df2,on="city",how="left")
# print(df3)
# df3 = pd.merge(df1,df2,on="city",how="outer")
# print(df3)
# If u want to know where it belongs to then use indicator.
# df3 = pd.merge(df1,df2,on="city",how="outer",indicator=True)
# print(df3)

# Another E.g
df1= pd.DataFrame({
    "city":["New york","Chicago","Orlando","baltimore"],
    "Temp":[21,14,35,32],
    "Humidity":[65,68,71,75]
})
# print(df1)

df2= pd.DataFrame({
    "city":["Chicago","New york","San diego"],
    "Temp":[21,14,35],
    "Humidity":[65,68,71]
})
# print(df2)

df3 = pd.merge(df1,df2,on="city",suffixes=('_left','_right'))
print(df3)

# Here extra columns will occur since columns are repeated in origin df1 and df2.
# If u want suffixes, of ur choice then u can use it.
import pandas as pd

india_weather = pd.DataFrame({
    "city" : ["mumbai","delhi","banglore"],
    "temperature" : [32,45,30],
    "humidity" : [80,60,78]
})
# print(india_weather)

us_weather = pd.DataFrame({
    "city" : ["new york","chicago","orlando"],
    "temperature" : [21,14,35],
    "humidity" : [68,65,75]
})
# print(us_weather)

# Now u want to join two dataframe, so panda provide us with concat option
# df=pd.concat([india_weather,us_weather])
# print(df)

# In this they are giving 0-2 index for both n u want continuous index for the full table.
# df=pd.concat([india_weather,us_weather], ignore_index=True)
# print(df)

# Now if u want the data separate by country in same table
# df=pd.concat([india_weather,us_weather], keys=["india","us"])
# print(df)
# print(df.loc["us"])

# 
# temperature_df = pd.DataFrame({
#     "city" : ["mumbai","delhi","banglore"],
#     "temperature" : [32,45,30]
# })
# print(temperature_df)

# # 
# windspeed_df = pd.DataFrame({
#     "city" : ["mumbai","delhi","banglore"],
#     "windspeed" : [7,12,9]
# })
# print(windspeed_df)

# df= pd.concat([temperature_df,windspeed_df])
# print(df)

# In this we will be getting temperature n windspeed but in temp row windspeed will be shown as NaN n vise versa
# df= pd.concat([temperature_df,windspeed_df],axis=1)
# print(df)

# If the sequence is changed then the sequence in output will change it will not take value or adjust according.
# If the row sequence changes than in anyone column might be temp or windspeed then?

# Now if u want to mold ur values according to sequence then?
# Give the index number.
temperature_df = pd.DataFrame({
    "city" : ["mumbai","delhi","banglore"],
    "temperature" : [32,45,30]
},index=[0,1,2])
# # print(temperature_df)

# # 
# windspeed_df = pd.DataFrame({
#     "city" : ["delhi","mumbai","banglore"],
#     "windspeed" : [7,12,9]
# },index=[1,0,2])
# # print(windspeed_df) 
# df= pd.concat([temperature_df,windspeed_df],axis=1)
# print(df)
# print(temperature_df)

s = pd.Series(["Humid","Dry","Rain"],name="event")
# print(s)
df = pd.concat([temperature_df,s],axis=1)
print(df)
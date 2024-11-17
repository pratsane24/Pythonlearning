import pandas as pd
# df = pd.read_csv("pandas/pivot.csv")

# # print(df)
# If u want print date in index and city column in rows then
# print(df.pivot(index="date",columns="city"))

# If u want to print only humidity then
# print(df.pivot(index="date",columns="city",values="humidity"))

# If u want humdity as index and column as cities
# print(df.pivot(index="humidity",columns="city"))

# Pivot table is used to summarize and aggregate data inside dataframe.

# df = pd.read_csv("pandas/pivot1.csv")
# print(df)
# print(df.pivot_table(index="city",columns="date"))

# If u want aggregate Sum then
# print(df.pivot_table(index="city",columns="date",aggfunc="sum"))

# If u want to get count
# print(df.pivot_table(index="city",columns="date",aggfunc="count"))
# print(df.pivot_table(index="city",columns="date",aggfunc="diff"))
# print(df.pivot_table(index="city",columns="date",aggfunc="mean"))
# print(df.pivot_table(index="city",columns="date",margins=True))
# Margins are giving aggregate of 2 nows in rows as well as in columns


# Now We have another set of data related to 1 city but of diiferent dates.
# Here we can apply grouper function to aggregate based on date frequency means let say u want 
# avg temp in a month of may and avg temp in month of dec. this can be done by using grouper function table.

df = pd.read_csv("pandas/pivot2.csv")
# print(df) 
df['date']=pd.to_datetime(df['date'])
# print(df)
# print(type(df['date']))
print(df.pivot_table(index=pd.Grouper(freq="M",key="date"),columns="city"))
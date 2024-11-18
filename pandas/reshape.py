# melt is used to transform or reshape data

import pandas as pd
# df = pd.read_csv("pandas/reshape.csv")
# print(df)

# df1=pd.melt(df,id_vars=["date"])
# print(df1)

# IF u want to filter out according to city u can do this also.
# print(df1[df1["variable"]=="Chicago"])

# If u want to change the column title
# df1=pd.melt(df,id_vars=["date"],var_name="city",value_name="temperatue")
# print(df1)

# df = pd.read_excel("pandas/stack.xlsx",header=[0,1])
# print(df)
# print(df.stack(level=0))

# If u want to unstack, and get original stack back
# df_stacked = df.stack()
# print(df_stacked)
# print(df_stacked.unstack())

# df2 = pd.read_excel("pandas/stack2.xlsx",header=[0,1,2])
# print(df2)
# print(df2.stack(level=2))


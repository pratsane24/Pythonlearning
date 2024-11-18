import pandas as pd
df = pd.read_excel("pandas/crosstab.xlsx")
# print(df)

# To call crosstab method we need to call pandas bze it is not on df
# print(pd.crosstab(df.Nationality,df.Handedness))
# print(pd.crosstab(df.Sex,df.Handedness,margins=True))

# I want more values in column like with sex,I want nationality also
# print(pd.crosstab(df.Sex,[df.Handedness,df.Nationality],margins=True))

# IF u want it at row level than?
# print(pd.crosstab([df.Nationality,df.Sex],[df.Handedness],margins=True))

# Sometimes it's good to have percentage
# Shift + Tab opens documentation on a method where mouse cursor is located.

# % at row level use value as index
# print(pd.crosstab([df.Sex],[df.Handedness],normalize='index'))

# U want to know avg age of female left handed n avg male whos are right handed.
# np is numpy so u need to import it
import numpy as np
print(pd.crosstab([df.Sex],[df.Handedness],values=df.Age, aggfunc=np.average))

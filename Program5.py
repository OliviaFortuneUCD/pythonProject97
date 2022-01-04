import pandas as pd
df1=pd.read_csv('Salary.csv')

df2=pd.read_csv('staff.csv')

df3=pd.read_csv('Percentage.csv')

# concatenating df1 and df2 along rows
vertical_concat = pd.concat([df1, df2,df3], axis=0)
# concatenating df3 and df4 along columns
horizontal_concat = pd.concat([df1, df2,df3], axis=1)

print(vertical_concat)
##print(horizontal_concat)
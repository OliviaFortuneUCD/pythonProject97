import pandas as pd
df1=pd.read_csv('Salary.csv')

df2=pd.read_csv('staff.csv')


df3 = (df1.merge(df2, left_on=['City', 'Country'], right_on=['City','Country']))
print(df3)
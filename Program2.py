import pandas as pd
staff  = pd.DataFrame({"Staff": ['Mary', 'John', 'Jack', 'Sally','Mark', 'Jane'],
                    "City": ['Dublin', 'Berlin', 'Warsaw', 'Paris','Dublin', 'Lisbon']})

salaries = pd.DataFrame({'City': ['Paris','Warsaw','Berlin','Dublin', 'London'],
                        'Avg Salary':[58000, 45000, 55000, 60000, 62000]})

# THe key is cities

newdf = staff.merge(salaries, left_on='City', right_on='City')
print(newdf)

otherdf = staff.merge(salaries, how='left')
print(otherdf)

staff_df = staff.merge(salaries, how='left')

print(staff_df[staff_df['Avg Salary'].isnull()])
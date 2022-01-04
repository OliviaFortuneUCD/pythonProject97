import pandas as pd

staff  = pd.DataFrame({"Staff": ['Mary', 'John', 'Jack', 'Sally','Mark', 'Jane'],
                       "City": ['Dublin', 'Berlin', 'Warsaw', 'Paris','Dublin', 'Lisbon'],
                       "Country": ['Ireland', 'Germany', 'Poland', 'France', 'US','Portugal']})

salaries = pd.DataFrame({'City': ['Paris','Warsaw','Berlin','Dublin', 'London', 'Paris', 'Dublin'],
                         'Country':['France', 'Poland','Germany','Ireland','London', 'US', 'US'],
                        'Avg Salary':[58000, 45000, 55000, 60000, 62000, 48000, 51000]})

m1= staff.merge(salaries, left_on=['City', 'Country'], right_on=['City','Country'])
print(m1)

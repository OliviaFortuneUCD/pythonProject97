import pandas as pd
q1  = pd.DataFrame({"Month": ['Jan', 'Feb', 'Mar'],
                    "Sales": [1200, 1000, 1100]})

q2  = pd.DataFrame({"Month": ['April', 'May', 'Jun'],
                    "Sales": [1300, 1400, 1350]})

newdf = pd.concat([q1,q2])
print(newdf)
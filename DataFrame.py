import pandas as pd
import numpy as np

data={
    'Age':[25,30,np.nan,35,np.nan],
    'Salary':[50000,54000,58000,np.nan,62000],
    'Gende':['M','F',np.nan,'F','M'],
    'Dept':['HR',np.nan,'IT','Finanace','IT']
}
print(data)
d=pd.DataFrame(data)
print(d)
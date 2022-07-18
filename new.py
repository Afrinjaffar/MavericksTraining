import pandas as pd
import numpy as np
import matplotlib as plt
import pandas.core.frame


data = pd.read_csv(r'C:\Users\mrafi\Downloads\Bank_churn_modelling - Copy.csv')
print(data)
# print(data.head(5))

out=pd.crosstab(data['Exited'],data['IsActiveMember'],margins=True)
print(out[1]/out['All'])





# out= pd.crosstab(data['Gender'],data['Exited'],margins=True)
# print(out)
# out1=pd.crosstab(data['sex'],[data['geography',data['exited']]],margins=True)
# print(out1)
# out=pd.crosstab(data)

# print(data['age'].apply(pd.to_numeric,errors='coerce').notnull().all(axis=1))

#print(data[data['Age'].str.isalpha()])
#print(data['Age'].head(17))



import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\mrafi\Downloads\insurance.csv')
print(data)
print(data.info())

print(data.describe())

print(data.isnull().sum())

print(data.drop_duplicates(keep='first', inplace=True))

print(data[data['charges'] == data['charges'].max()])

print(data[data['charges'] == data['charges'].min()])

print(data.corr())

print(data['charges'].groupby(data['smoker']).mean())

print(data.groupby(['smoker', 'sex']).count()['age'])

print(data.groupby(['smoker', 'sex']).mean()/data.shape[0])

print(data.groupby(['bmi', 'age']).mean()/data.shape[0])

print(data.groupby(['bmi', 'smoker']).mean()['charges']/data.shape[0])

print(data.groupby(['bmi', 'age','smoker']).mean()['charges']/data.shape[0])

print(data.groupby(['age', 'region','smoker']).mean()['charges']/data.shape[0])

print(data.groupby(['age', 'children','region','smoker']).mean()['charges']/data.shape[0])













#out1=pd.crosstab(data['children'],data['region'],values=data['charges'],aggfunc=np.mean)

#print(out1.count()/data.shape[0])

#out1=pd.crosstab(data['children'],data['bmi'],values=data['charges'],aggfunc=np.mean)

#print(out1.count()/data.shape[0])



























#print(data[['temperature', 'energy_output']].corr())

#









#print(out1.max())










#print(data['charges'].mean())
#print(data['charges'].median())
#print(data.pivot_table(index='sex',columns='children'))
#print(data.pivot_table(index='smoker',columns='age',values='charges', aggfunc =np.std))
#print(data.pivot_table(index='children',columns='region',values='bmi', aggfunc =np.mean))



#print(data.pivot)















# print(data['age'].var())
# print(data['age'].std())
# print(data[['age', 'bmi']].cov())
# print(data[['age', 'bmi']].corr())
# print(data['age'].quantile(0.25))
# print(data['age'].quantile(0.50))
# print(data['age'].quantile(0.75))
# print(data.head(5))
# print(data[['age', 'bmi', 'children']].count())
# print(data.describe())
# print(data.describe().T)
# print(data.query('5*age>50'))
# print(data.query('sqrt(age)>5'))
# print(data.query('age>30 and sex=="female"'))
# assign= lambda n:n+5 if n<20 else n
# data['bmi'] = data['bmi'].apply(assign)
# print(data)

# out=pd.crosstab(data['smoker'],data['sex'],values=data['charges'],aggfunc=np.average)
# print(out)

# out1=pd.crosstab(data['bmi'],data['sex'],values=data['charges'],aggfunc=np.average)
# print(out1)

#g = data.groupby('region')

#print(g)
#for region, dataframe in g:
    #print(region)
    #print(dataframe)

#print(g.max)
#print(g.count)

#southeast= g.get_group('southeast')
#print(southeast)

#out=pd.set_option('display.max_columns',100)
#print(out)

#data=data.sort_values()





#b=data['charges']
#data=data.drop('charges',axis=1)
#print(data.head())

#data.insert(3,'charges1',b)
#print(data.head())

#data.insert(3,'charges2',b)
#print(data.head())



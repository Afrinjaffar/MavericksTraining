from collections import Counter
from itertools import combinations

import pandas as pd

data = pd.read_csv(r'C:\Users\mrafi\Downloads\DA Project using Pandas(sales data)\sales-data.csv')
# print(data)
print(data.head())

# 1.What was the best month for sales? How much was earned that month?
data['Total Sales'] = data['Quantity Ordered'] * data['Price Each']
print(data['Total Sales'])
print(data.groupby('Month').sum())

# 2.What city sold the most product?
data['City'] = data['Purchase Address'].apply(lambda n: n.split(',')[1])
print(data['City'])
print(data.groupby('City').sum())

# 3.What time should we display advertisemens to maximize the likelihood of customer’s buying product?
data['Order Time'] = pd.to_datetime(data['Order Date'])
print(data['Order Time'])
data['Time'] = data['Order Time'].dt.hour
print('Time')
print(data.groupby('Time').count())



#4.What products are most often sold together?

new = data[data['Order ID'].duplicated(keep=False)]
new['Product_grp'] = new.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
new = new[['Order ID', 'Product_grp']].drop_duplicates()
print(new.head(2))




#5.What product sold the most? Why do you think it sold the most?
product_grp=data.groupby('Product')
print(product_grp.sum())














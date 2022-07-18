import numpy as np
import pandas as pd
from torch.utils.data.datapipes import dataframe

df2 = pd.read_csv(r'C:\Users\mrafi\Downloads\zomato.csv', encoding="ISO-8859-1")
print(df2)

df3 = pd.read_csv(r'C:\Users\mrafi\Downloads\CountryCode.csv')
print(df3)

#1.Which restaurant has the largest number of votes from the customer?
#max_votes = df2.loc[df2['RestaurantName'].idxmax()]
#print(max_votes)

#3.Which city is costliest in each country?
#data4 = pd.merge(df2, df3, on='cc', how='inner')
#print(data4)
#out1 = pd.crosstab(data4['Country'], data4['City'], values=data4['Price range'],aggfunc=np.mean)
#print(out1)


#4. In india how many restaurants are present in each locality?
#data3 = pd.merge(df2, df3, on='cc', how='inner')
#print(data3)
#grp = data3.groupby('Country')
#for City,dataframe in grp:
   # print(City)
  # print(dataframe)
#india = grp.get_group('India')
#print(india)
#print(india.head()))

#5.Which city has the most number of restaurants in each country?
 #data = pd.merge(df2, df3, on='cc', how='inner')
 #print(data)
 #group = df2.groupby(['City']).size().reset_index(name='No of Restaurant')
 #print(group)

# 6.Which franchise has the highest number of Restaurants?
 #data = df2.groupby(["Restaurant Name"]).size().reset_index(name='Restaurant Count').max()
 #print(data)


#7.How many Restaurants are accepting online orders?

g1 = df2.groupby('Has Online delivery')
print(g1)
for HasOnlinedelivery, dataframe in g1:
 print(HasOnlinedelivery)
print(dataframe)
restaurant = g1.get_group('Yes')
print(restaurant)



#8.How many have a book table facility?
 #print(df2['Has Table booking'].value_counts()


#9.Which location has the highest number of Restaurants?
 #data = df2.groupby(["City"]).size().reset_index(name='Restaurant Count').max()
 #print(data)


#10.How many types of Restaurant types are there?
 #print(df2['Restaurant Name'].nunique())


#11.What is the most liked Restaurant type?
 #out = pd.crosstab(df2['Restaurant Name'], df2['Votes'], values=df2['Price range'], aggfunc=np.average)
 #print(out)


#12.What is the Average cost for 2 persons?
 #g=df2.groupby('Average Cost for two')
 #print(g)
 #for AverageCostfortwo, dataframe in g:
 #print(AverageCostfortwo)
 #print(dataframe)
 #AverageCostfortwo=g.get_group('Average Cost for Two')
 #print(AverageCostfortwo))


#13.What is the most liked Dish type?
 #out = pd.crosstab(df2['Cuisines'], df2['Votes'], values=df2['Price range'], aggfunc=np.average)
 #print(out)




engine= pyodbc.connect('Driver={SQL SERVER};'
                                  'Server=DESKTOP-NLNS7S5;'
                                  'Database=insurance;'
                                  'Trusted_Connection=yes;')


conn = pyodbc.connect('Driver={SQL SERVER};'
                      'Server=DESKTOP-NLNS7S5;'
                      'Database=Python;'
                      'Trusted_Connection=yes;'
                      )
cursor = conn.cursor()
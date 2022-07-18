import pandas as pd
import numpy as np
import os
import glob
data1 = pd.read_csv(r'C:\Users\mrafi\Downloads\instanceUsage_data (1).csv')
#print(data1)
data2 = pd.read_csv(r'C:\Users\mrafi\Downloads\instanceEvent_data.csv',chunksize=100000)
df=pd.DataFrame()
for i in data2:
    print(i.size)
    df.append(i)




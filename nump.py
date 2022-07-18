import activate as activate
import pandas as pd
import numpy as np
import cv2
import cv2_plt_imshow
import pip
from matplotlib.image import imread
import sys


df = pd.DataFrame([[34, 56], [66, 78], [88, 98]])
print(df)

#data = df.sum(axis=1)
#print(data)
# print(df.mean(axis=1))
# print(df.max(axis=1))
# print(df.var(axis=0))

# print(df > 100)

#a=np.ones([3,3])
#print(a)
#b = np.arange(0,20,3)
#print(b)

#a=np.eye(3)
#print(a)
#print(np.sin(df))
#print(np.log(df))
#print(np.sqrt(df))
#print(np.round(df))
#a=np.delete(df, 1, axis=0)
#print(a)
#a=np.linspace(0,50,10)
#print(a)


img = cv2.imread(r'C:\Users\mrafi\OneDrive\Pictures\Certificate of completion of Database courses.png')

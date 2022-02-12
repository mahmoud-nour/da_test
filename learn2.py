# import os
# os.getcwd()
# os.path.abspath(__file__)
# os.path.dirname(os.path.abspath(__file__))

# from random import randint


# def checkName(name):
#   return name.lower().startswith("a")

# myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

# myReturnedData = filter(checkName, myTexts)

# for person in myReturnedData:

#   print(person)

# print("#" * 50)

# randint(50,100)

# from PIL import Image
# myimg=Image.open('11.jpg')
# myimg.show()

from datetime import datetime
import numpy as np
import pandas as pd
# import seaborn as snc
# import statistics
# sample = [1, 3,12,4,7,12,2]
# ds=pd.Series(sample)
# ds.describe()
# # ds.sort_values()

# print("Standard Deviation of sample is % s "
#                 % (statistics.stdev(sample))**2)
# df=pd.read_csv('DataFiles\\Salaries.csv')
# df
# snc.countplot()

# a=np.random.randint(0,10,9).reshape(3,3)
# b=np.random.randint(0,10,9).reshape(3,3)
# a,b,np.sort(a,axis=0),np.linalg.inv(a)
# np.polyint(np.poly1d((2,2)),2)

x=np.datetime64('2019-02-24')
y=np.arange(10)
x-y
x*y


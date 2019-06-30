import pandas as pd
import numpy as np
#Read csv file
df = pd.read_csv("Automobile.csv")

#Handle the missing values for Price column
df['price'] = df['price'].fillna(df['price'].mean())

#Get the values from Price column into a numpy.ndarray
list1 = df['price'].tolist()
price = np.array(list1)
print(type(price))

#Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
minn = df['price'].min()
maxx = df['price'].max()
meann = df['price'].mean()
stdd = df['price'].std()
print('Mininmum price = ',minn)
print('Maximum price = ',maxx)
print('Mean price = ',meann)
print('Standard Deviation of price = ',stdd)
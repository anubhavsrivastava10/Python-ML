import pandas as pd
import numpy as np
#apyrio is a .py file not in a the library
from apyori import apriori
import matplotlib.pyplot as plt

#read the dataset
dataset = pd.read_csv('BreadBasket_DMS.csv')

#draw the pie chart of top 15 selling items
item = dataset['Item'].value_counts().head(15)
labels = item.keys()
plt.pie(item,labels=labels)

#removing rows with value NONE in it
dataset = dataset.replace(to_replace='NONE', value=np.nan).dropna()

#make a single row for every transaction
s = dataset.groupby('Transaction')['Item'].apply(list)
#converting series to list
d = s.tolist()

#using apirio to find the related
rules = apriori(d, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

#making it into a list because it is a generator
result = list(rules)

#reading item from the list
for item in result:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    #printing the associated items only
    print("Rule: " + items[0] + " -> " + items[1])
    print("=====================================")
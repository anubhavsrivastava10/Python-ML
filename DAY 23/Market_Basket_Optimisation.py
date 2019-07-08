import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

#reading dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

#converting dataset to list
List_dataset = dataset.values.tolist()

#creating an empty list
z=[]
#converting all the data in dataset to one list
for x in List_dataset:
    z.extend(x)

#removing all the nan values from the list
cleanedList1 = [q for q in z if str(q) != 'nan']

#find the top 10 edibles
data= pd.DataFrame(cleanedList1)

#finding the top 10 item 
item = data[0].value_counts().head(10)
labels = item.keys()
x_index = [1,2,3,4,5,6,7,8,9,10]

#plotting the bar graph
plt.bar(x_index, item)

plt.xticks(x_index,labels,fontsize=10, rotation=45)
plt.ylabel('count')
#showing the bar graph
plt.show()

#created an empty list
new_L=[]

#removing nan value and appending data in that empty list
for item in List_dataset:
    cleanedList = [x for x in item if str(x) != 'nan']
    new_L.append(cleanedList)
    
# Training Apriori on the dataset
rules = apriori(new_L, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

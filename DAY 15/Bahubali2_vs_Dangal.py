import pandas as pd

#reading the dataset
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
#checking for any null values
dataset.isnull().any(axis=0)

#prepare the data to train the model
features = dataset.iloc[:, :1].values  
labels_B = dataset.iloc[:, 1:2].values
labels_D = dataset.iloc[:, 2:3].values

#and then the trainig the bahubali model
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels_B) 

#train the algo for Dangal
regressor1 = LinearRegression()  
regressor1.fit(features, labels_D) 

#predicting the collection on day 10 for Dangal
x = regressor1.predict(10)
#predicting the collection on day 10 for Bahubali
y = regressor.predict(10)

#checking which movie collected more
if x>y:
    print('Dangal collected more')
else:
    print('Bahubali collected more')
    
print('Dangal Collection on Day 10 ' + str(x))
print('Bahubali Collection on Day 10 ' + str(y))

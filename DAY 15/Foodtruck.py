import pandas as pd

#reading the dataset
dataset = pd.read_csv('Foodtruck.csv')
#checking for any null values
dataset.isnull().any(axis=0)

#prepare the data to train the model
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

#and then the train test split
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#predicting the outlet profict or loss if population is 3.073 million
regressor.predict(3.073)

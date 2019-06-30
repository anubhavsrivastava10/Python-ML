import pandas as pd

#reading txt file and assigning coloumn names
dataset = pd.read_csv('Auto_mpg.txt', delimiter= '\s+', index_col=False, names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])

features = dataset.iloc[:,1:8]
labels = dataset.iloc[:,0].values

#replacing missing value with 0
features = features.replace('?',0)
#changing the object type to float
features.horsepower = features.horsepower.astype(float).fillna(0.0)

#performing train test and spliy
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size = 0.2, random_state=0)

#making a Decision Tree (regression)
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(features_train,labels_train)

#performing prediction on the testing data
labels_pred = regressor.predict(features_test)

df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  

#making a random forest(regression)

#feature scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

#train the model
from sklearn.ensemble import RandomForestRegressor

regressor1 = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor1.fit(features_train, labels_train)  
labels_pred1 = regressor1.predict(features_test)  

df1=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred1})  
df1  

from sklearn import metrics  
#error in the decision_tree
print('Mean Absolute Error of decision tree : ', metrics.mean_absolute_error(labels_test, labels_pred))
#error in the random_forest
print('Mean Absolute Error of random forest : ', metrics.mean_absolute_error(labels_test, labels_pred1))

#Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
import numpy as np
x = [6,215,100,2630,22.2,80,3]
x = np.array(x)
x = x.reshape(1,7)
#prediction from the decision tree
regressor.predict(x)
#prediction from the random forest
regressor1.predict(x)

#finding the car name with maximum mpg
dataset['car name'].loc[dataset['mpg'].idxmax()]

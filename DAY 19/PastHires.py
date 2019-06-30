import pandas as pd

#reading data
dataset = pd.read_csv('PastHires.csv')

#assigining features and labels
features = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1]

#given Y:1 and N:0 and BS:1 and MS:2 and PhD:3
features['Interned'] = features['Interned'].map({'Y': '1', 'N': '0'})
features['Top-tier school'] = features['Top-tier school'].map({'Y': '1', 'N': '0'})
features['Employed?'] = features['Employed?'].map({'Y': '1', 'N': '0'})
features['Level of Education'] = features['Level of Education'].map({'BS': '1', 'MS': '2' , 'PhD': '3'})

#features['Level of Education'] = features['Level of Education'].astype(float)

#dividing training and testing data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#training data for making predictions
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(features_train,labels_train)

#predicting the data
labels_pred = classifier.predict(features_test)
new_pred = pd.Series(labels_pred)

#making a confusion matrix to check precision
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,new_pred))

#Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
import numpy as np
x = [10,1,4,1,1,0]
x = np.array(x)
x = x.reshape(1,6)
classifier.predict(x)

#Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
y = [10,0,4,1,0,1]
y = np.array(y)
y = y.reshape(1,6)
classifier.predict(y)
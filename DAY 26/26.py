import pandas as pd
import numpy as np
from sklearn import metrics

#importing the dataset
dataset_test = pd.read_csv('test.csv')
dataset_train = pd.read_csv('train.csv')
 
features_test = dataset_test.iloc[:,:-1]
features_train = dataset_train.iloc[:,:-1]
labels_test = dataset_test.iloc[:,-1]
labels_train = dataset_train.iloc[:,-1]

#list for storing score for normal features
n_f = []
#list for storing score for reduced features
r_f = [] 

#--------------------------------------------------------------------------------------------
#Training and making predictions using Decision Tree
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
n_f.append(acc)

#--------------------------------------------------------------------------------------------------
#Training and making predictions using Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
n_f.append(acc)

#---------------------------------------------------------------------------------------------------
#Training and making predictions using KnN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 13, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
n_f.append(acc)


#-------------------------------------------------------------------------------------------------

#Training and making predictions using Random Forest for entropy
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=25, random_state=0, criterion = 'entropy')  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)  

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
n_f.append(acc)

#---------------------------------------------------------------------------------------------------

#Training and making predictions using Random Forest for gini
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=25, random_state=0, criterion = 'gini')  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)  

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
n_f.append(acc)

#by the score we can see that score of entropy is more so entropy is better than gini

#-----------------------------------------------------------------------------------------------

#feature selection

#labelencoded the labels os can be used in the backward elimination process
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels_ = le.fit_transform(labels_train)
# add code to automate the p value removing
import statsmodels.api as sm

#using backward elemination to reduce the number of features
features_obj = features_train.iloc[:,:].values
features_obj = sm.add_constant(features_obj)
cols= list(range(features_obj.shape[1]))
while (True):
    regressor_OLS = sm.OLS(endog = labels_,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        val = p_values.argmax()
        features_obj = np.delete(features_obj,val,1)
        cols.pop(val)
    else:
        break

#changing the number of test features for the test data
features_obj_test = features_test.iloc[:,:].values
features_obj_test = features_obj_test[:,cols]
#changing the number of features fot the training data
features_obj_train = features_train.iloc[:,:].values
features_obj_train = features_obj_train[:,cols]

#--------------------------------------------------------------------------------------------
#Training and making predictions using Decision Tree
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_obj_train, labels_train)

labels_pred = classifier.predict(features_obj_test)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
r_f.append(acc)


#--------------------------------------------------------------------------------------------------
#Training and making predictions using Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_obj_train, labels_train)

# Predicting the class labels
labels_pred = classifier.predict(features_obj_test)

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
r_f.append(acc)

#---------------------------------------------------------------------------------------------------
#Training and making predictions using KnN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 13, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_obj_train, labels_train)

# Predicting the class labels
labels_pred = classifier.predict(features_obj_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
r_f.append(acc)


#-------------------------------------------------------------------------------------------------

#Training and making predictions using Random Forest for entropy
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=25, random_state=0, criterion = 'entropy')  
classifier.fit(features_obj_train, labels_train)  
labels_pred = classifier.predict(features_obj_test)  

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
r_f.append(acc)

#---------------------------------------------------------------------------------------------------

#Training and making predictions using Random Forest for gini
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=25, random_state=0, criterion = 'gini')  
classifier.fit(features_obj_train, labels_train)  
labels_pred = classifier.predict(features_obj_test)  

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

#finding the score of the model
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, labels_pred)
r_f.append(acc)

#---------------------------------------------------------------------------------------------

#plotting the graph for the score with feature reduction and without feature reduction

import matplotlib.pyplot as plt
#creating object
objects = ('decision tree' , 'Logistic regression', 'kNN' , 'RF entropy', 'RF gini')
x_index=[0,1,2,3,4]

#creating distance with the bars
bar = 0.3
r1 = np.arange(len(objects))
r2 = [x + bar for x in r1]

#plotting the bar graph
plt.bar(r1,n_f, color='blue',label = 'normal feature', align='center')
plt.bar(r2,r_f, color='red', label = 'reduced feature', align='center')
plt.xticks(rotation=70)

plt.xticks(x_index, objects)
plt.legend()

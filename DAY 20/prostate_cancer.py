import pandas as pd

dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

features = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1]

#performing train test and spliy
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size = 0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = regressor.predict(features_test)

import numpy as np
labels_test = np.array(labels_test)

#yes we can predict lspa
df = pd.DataFrame(labels_test,labels_pred)
df

#(1) Train the unregularized model (linear regressor) and calculate the mean squared error.

 
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, labels_pred),2) )

#(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

lm_lasso = Lasso() 
lm_ridge =  Ridge() 

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

predict_test_lasso = lm_lasso.predict (features_test)
predict_test_ridge = lm_ridge.predict (features_test)

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (metrics.mean_squared_error(predict_test_lasso,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (metrics.mean_squared_error(predict_test_ridge,labels_test)*100,2))

#(b) Can we predict whether lpsa is high or low, from other variables?

mean_val = dataset['lpsa'].mean()

labels = labels.to_frame()
labels['lpsa'] = labels['lpsa'].map(lambda x : 1 if x > mean_val else 0)

#performing train test and spliy
from sklearn.model_selection import train_test_split
features_train1, features_test1, labels_train1, labels_test1 = train_test_split(features,labels,test_size = 0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train1 = sc.fit_transform(features_train1)
features_test1 = sc.transform(features_test1)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train1, labels_train1)

# Predicting the Test set results
labels_pred = classifier.predict(features_test1)

import numpy as np
labels_test = np.array(labels_test1)

#yes we can predict lspa
df2 = pd.DataFrame(labels_test1,labels_pred)
df2

#making confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test1,labels_pred)
cm
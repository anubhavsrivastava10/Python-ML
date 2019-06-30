import pandas as pd

dataset = pd.read_csv('kc_house_data.csv')

#finding null value
dataset.isnull().any()

#filling the nan value
dataset['sqft_above']=dataset['sqft_above'].fillna(dataset['sqft_above'].mean())

dataset['date'] = dataset['date'].str.replace('T','0')

dataset['date'] = dataset['date'].astype(float)

labels = dataset['price']
features = dataset.drop('price',axis =1 )

#performing train test and spliy
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size = 0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#• Use Linear Regression and see the results

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

#• Use Lasso (L1) and see the resuls
from sklearn.linear_model import Lasso

lm_lasso = Lasso()
# Fit x_train and y_train
lasso = lm_lasso.fit(features_train, labels_train)

#predicting
predict_test_lasso = lm_lasso.predict (features_test)

df1 = pd.DataFrame(labels_test,predict_test_lasso)
df1

#• Use Ridge and see the score

from sklearn.linear_model import Ridge

lm_ridge = Ridge()

#fitting
ridge = lm_ridge.fit(features_train,labels_train)

#predicting
predict_test_ridge = lm_ridge.predict(features_test)

#finding score
print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

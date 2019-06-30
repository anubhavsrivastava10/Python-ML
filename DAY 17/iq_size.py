import pandas as pd

#reading the csv file
dataset = pd.read_csv('iq_size.csv')

#definign features and labels
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, 0].values
                     
#checking for null values
dataset.isnull().any(axis=0)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train,  features_test, labels_train, labels_test = train_test_split(features , labels ,test_size = 0.1 , random_state =0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train , labels_train)

# Predicting the Test set results
Pred = regressor.predict(features_test)

#matching the predicted data with the actual data
# print (pd.DataFrame(Pred, labels_test))

#What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ?
import numpy as np
x = [90,70,150]
x = np.array(x)
x = x.reshape(1,-1)
y = regressor.predict(x)
y = int(y)
print("IQ of the person is : " + str(y))


import statsmodels.api as sm
features = sm.add_constant(features)


features_opt = features[:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

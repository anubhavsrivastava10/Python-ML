import pandas as pd

#reading the csv file
dataset = pd.read_csv('University_data.csv')

#checking for any null values
dataset.isnull().any(axis=0)

#defining features and labels
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

# Encoding categorical data(text data)
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

# Onehot Encoding the Categorical data
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()


# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.1, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)

# Predicting the Test set results
Pred = regressor.predict(features_test)

import pandas as pd
#matching the data with the actual data
print (pd.DataFrame(Pred, labels_test))

#taking input recquired
le1 = input("Enter the College name from(Cabrini , BeaverAlbany, Maryland , Alaska Methodist University) : ")
gre = int(input("Enter your GRE Score : "))
sop = float(input("Enter SOP : "))
lor = float(input("Enter LOR : "))
cgpa = float(input("Enter CGPA : "))
research = int(input("Enter Research : "))


import numpy as np
le = labelencoder.transform([le1])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],gre,sop,lor,cgpa,research]
x = np.array(x)
x = x.reshape(1,-1)

#predicting the chances
regressor.predict(x)

#checking the accuracy for training data
Score = regressor.score(features_train, labels_train)
print(Score)
#checking the accuracy for training data
Score = regressor.score(features_test, labels_test)
print(Score)


import pandas as pd

dataset = pd.read_csv('affairs.csv')

features = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1]


#performing one hot encoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
features = onehotencoder.fit_transform(features).toarray()
features = features[:,1:]
onehotencoder1 = OneHotEncoder(categorical_features = [-1])
features = features[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

perc = ((cm[0][1]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1]))*100
print("% of Females having affairs : " + str(perc))

#Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.
import numpy as np
x = [3,25,3,1,4,3,2,2]
x = np.array(x)
x = x.reshape(1,8)
ohe = onehotencoder.transform(x).toarray()
ohe = ohe[0][1:]
ohe = ohe.reshape(1,12)
ohe1 = onehotencoder1.fit_transform(ohe).toarray()
ohe1 = ohe1[0][1:]
ohe1 = ohe1.reshape(1,11)

print(classifier.predict(ohe1))
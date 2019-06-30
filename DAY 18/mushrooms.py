import pandas as pd

dataset = pd.read_csv('mushrooms.csv')

features_h = dataset.iloc[:,-1]
features_p = dataset.iloc[:,-2]
features_o = dataset.iloc[:,5]
labels = dataset.iloc[:,0]
features_h = features_h.to_frame()
features_p = features_p.to_frame()
features_o = features_o.to_frame()
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features_h.values[:,0] = labelencoder.fit_transform(features_h.values[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features_h = onehotencoder.fit_transform(features_h).toarray()

features_p.values[:, 0] = labelencoder.fit_transform(features_p.values[:, 0])
features_p = onehotencoder.fit_transform(features_p).toarray()
features_o.values[:, 0] = labelencoder.fit_transform(features_o.values[:, 0])
features_o = onehotencoder.fit_transform(features_o).toarray()



#combine all features









# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = regressor.predict_proba(features_test)

# Predicting the class labels
labels_pred = regressor.predict(features_test)

#checking the predicted data with the actual data
pd.DataFrame(labels_pred, labels_test)

#making a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

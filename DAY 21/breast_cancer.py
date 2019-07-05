import pandas as pd

#reading the csv file
dataset = pd.read_csv('breast_cancer.csv')

#making the features and labels
features = dataset.iloc[:,1:-1]
labels = dataset.iloc[:,-1]

#finding the null value if any
features.isnull().any()
labels.isnull().any()

#finding the most frequent number
values = features['G'].value_counts().keys().tolist()

#replacing the nan value with the most frequent value
features.G = features.G.fillna(values[1])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Model Score
score = classifier.score(features_test,labels_test)
print("Accuracy of the model is : " + str(score))

#predicting the value by the given condition
import numpy as np
x = [6,2,5,3,9,4,7,2,2]
x = np.array(x)
x = x.reshape(1,9)
predict = classifier.predict(x)
if predict == 4:
    print("Malignant")
else:
    print("Benign")
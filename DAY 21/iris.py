#importing iris from the sklearn
from sklearn.datasets import load_iris
dataset = load_iris()

#train_test_split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(dataset.data, dataset.target, test_size = 0.3 , random_state=0)

#using SVM
#fitting the data using SVM
from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train,labels_train)

#predicting the data
labels_pred = classifier.predict(features_test)

#finding the accuracy of the model
score = classifier.score(features_test,labels_test)
print(score)
import pandas as pd

dataset = pd.read_csv('bluegills.csv')

labels = dataset.iloc[:,1]
features = dataset.iloc[:,0]
features = features.to_frame()
labels = labels.to_frame()

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

import matplotlib.pyplot as plt
# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features,regressor.predict(features) , color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Length')
plt.ylabel('Age')
plt.show()

regressor.predict(5)
#Visualising the Polynomial Regression Results
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly,labels )

print ("Predicting result with Polynomial Regression")
print (lin_reg_2.predict(poly_object.transform(5)))


plt.scatter(features,labels , color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Length')
plt.ylabel('Age')
plt.show()


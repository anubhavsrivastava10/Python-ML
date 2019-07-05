#importing recquired
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#reading the dataset
dataset = pd.read_csv('tshirts.csv')

#creating features
features = dataset.iloc[:,1:].values

#scattering the points of the features to analyze the data
plt.scatter(features[:,0],features[:,1])
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

#finding the number of clusters usimg elbow method

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_) 

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

#as we can see there are two elbows but according to the given statment we have 3 clusters

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

#visualizing the data
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1] , c='blue' , label='large')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1] , c='red' , label='medium')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1] , c='pink' , label='small')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.show()
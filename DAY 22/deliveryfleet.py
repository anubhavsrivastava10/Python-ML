#import the recquired
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#reading the given dataset
dataset = pd.read_csv('deliveryfleet.csv')

#defining features
features = dataset.iloc[:,1:].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

#using the elbow method to find the exact number of clusters to be formed

#creating an empty list
wcss = []
for i in range(1, 11):
    #making the clusters with the number given by i
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    #fitting the data according to the number of clusters
    kmeans.fit(features)
    #storing the value in the wcss
    wcss.append(kmeans.inertia_)
    
#Now plot it to find where there is a sudden change or where the elbow is formed       
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
#we get there are 2 clusters 

# Fitting K-Means to the dataset with the n_clusters = 2
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.xlabel('Distance_feature')
plt.ylabel('Speeding_feature')
plt.legend()
#by the plot we can see that the rural are overspeeding more and urban are moving on a limited speed

#divide the rural and urban if they are following the speed limit or not

#dividing them into 4 clusters
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans.fit_predict(features)

#visualizing the clusters
plt.scatter(features[pred_cluster1 == 0, 0], features[pred_cluster1 == 0, 1], c = 'blue', label = 'Rural following speed')
plt.scatter(features[pred_cluster1 == 1, 0], features[pred_cluster1 == 1, 1], c = 'red', label = 'Urban following speed')
plt.scatter(features[pred_cluster1 == 2, 0], features[pred_cluster1 == 2, 1], c = 'pink', label = 'Urban not following speed')
plt.scatter(features[pred_cluster1 == 3, 0], features[pred_cluster1 == 3, 1], c = 'black', label = 'Rural not following speed')
plt.xlabel('Distance_feature')
plt.ylabel('Speeding_feature')
plt.legend()

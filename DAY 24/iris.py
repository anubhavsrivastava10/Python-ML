import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
iris=iris.data

df = pd.DataFrame(iris)
features = df.iloc[:].values
                
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_ = sc.fit_transform(features)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_ = pca.fit_transform(features_)

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features_)


# Visualising the clusters
plt.scatter(features_[pred_cluster == 0, 0], features_[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features_[pred_cluster == 1, 0], features_[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features_[pred_cluster == 2, 0], features_[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()

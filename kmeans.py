
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

def kmeans_func(path,clust_num):
    data = pd.read_csv(path)
    n = len(data.columns)

    columns = [i for i in range(n-1)]
    x = data.iloc[:, columns].values

    n = len(data.columns)
    variety = data.columns[n-1]
    classes = unique_values(data[variety])
    
    data_classes = []
    for i in range (len(classes)):
        data_classes.append([classes[i],data.loc[data[variety]==classes[i]]])


    kmeans = KMeans(n_clusters = clust_num, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    y_kmeans = kmeans.fit_predict(x)

    #Visualising the clusters
    colors = ['blue','green','yellow','purple','orange','black']
    for i in range(len(classes)):
        plt.scatter(x[y_kmeans == i, 0], x[y_kmeans == i, 1], s = 20, c = colors[i], label = classes[i])

    #Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 50, c = 'red', label = 'Centroids')

    plt.legend()

    '''# 3d scatterplot using matplotlib

    fig = plt.figure(figsize = (15,15))
    ax = fig.add_subplot(111, projection='3d')
    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'purple', label = 'Iris-setosa')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'orange', label = 'Iris-versicolour')
    plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

    #Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'red', label = 'Centroids')'''

    plt.show()

def elbow_method(path,clust_max):
    data = pd.read_csv(path)
    n = len(data.columns)
    columns = [i for i in range(n-1)]
    x = data.iloc[:, columns].values
    wcss = []
    for i in range(1, clust_max):
        kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, clust_max), wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS') 
    plt.show()


def unique_values(list): #get every values in a list

    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


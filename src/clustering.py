from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np 


def plot_silhouette_scores(model, data, n_clusters_list, metric='euclidean'):
    """plot silhouette scores
    Args:
        model (sklearn model): model to use for clustering
        data (array-like, sparse matrix): of shape (n_samples, n_features)
        n_clusters_list (list): list of number of clusters to use
        metric (str): metric to use for clustering
    
    Returns:
        fig (matplotlib figure): figure
        ax (matplotlib axes): axes
    """

    for k in n_clusters_list:
        fig, ax = plt.subplots(1,1)
        # silhoutte score
        ax.set_xlim([0,1])
        ax.set_ylim([0, len(data) + (k+1)*10])  
        ax.set_xlabel('Silhouette Score')
        ax.set_ylabel('Cluster')
        ax.set_title(f'Silhouette Score for {k} clusters')


        # clustering 
        model.set_params(n_clusters=k)
        cluster_labels = model.fit_predict(data)
        silhouette_avg = metrics.silhouette_score(data, cluster_labels, metric=metric)
        print(f"For n_clusters = {k}, The average silhouette_score is : {silhouette_avg: .2%}")

        # sample silhouette plot
        sample_silhouette_values = metrics.silhouette_samples(data, cluster_labels, metric=metric)
        y_lower = 10

        # iterate over clusters 
        for i in range(k):
            ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / k)
            ax.fill_betweenx(np.arange(y_lower, y_upper),
                            0, ith_cluster_silhouette_values,
                            facecolor=color, edgecolor=color, alpha=0.7)

            ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            y_lower = y_upper + 10

        ax.axvline(x=silhouette_avg, color="red", linestyle="--")
        ax.set_yticks([])
        ax.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        plt.show()

    return fig, ax


# Hopkins' statistic 

def hopkins(data):
    """
    Compute the Hopkins statistic on a given dataset.
    Parameters
    based on this paper: 

    from this article: 
    https://www.datanovia.com/en/lessons/assessing-clustering-tendency/#statistical-methods

    Args:
    data : array-like
        Observations of a random variable.
    Returns:
        h (float): The Hopkins statistic.
    """
    pass 

def elbow(data, max_n_clusters=15, kmeans_kws=None):
    """plot the sum of squares with the silhouette scores 
    for different number of clusters < max_n_clusters
    in order to use the elbow method to determine the optimal number of clusters
    No preprocessing is done for data.

    Args: 
        data (array-like, sparse matrix): of shape (n_samples, n_features)
        max_n_clusters (int): max number of clusters to form
        kmeans_kws (dict): dictionary of kwargs to pass to the KMeans algorithm.
    
    Returns:
        fig (matplotlib figure): figure
        ax (matplotlib axes): axes
    """
    Sum_of_squared_distances = []
    sil_scores = []
    K = range(1, max_n_clusters)
    kwargs = {
        'n_init': 100,
        'max_iter': 1000, 
        'random_state': 2022, 
        'algorithm': 'full'
    } if kmeans_kws is None else kmeans_kws

    for k in K:
        km = KMeans(n_clusters=k, **kwargs)
        km = km.fit(data)
        # labels 
        cluster_labels = km.labels_
        Sum_of_squared_distances.append(km.inertia_)

        if k>1:
            sil_avg = metrics.silhouette_score(data, cluster_labels)
            sil_scores.append(sil_avg)

    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(K, Sum_of_squared_distances, 'bx-')
    ax.set_ylabel('Sum_of_squared_distances')
    ax.set_xlabel('k')


    ax2 = ax.twinx()
    ax2.plot(K[1:], sil_scores, 'ro-')

    # legends 
    fig.legend((ax.lines[0], ax2.lines[0]), 
            ('Sum_of_squared_distances', 'Silhouette Score'), 
            bbox_to_anchor=(0.5, -0.05), loc='lower center',
            ncol=2)

    fig.suptitle('Elbow Method For Optimal k')
    fig.tight_layout()

    return fig, ax
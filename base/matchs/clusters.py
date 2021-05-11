import abc


class Cluster:

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def clustering(self):
        """

        Returns:

        """

    def add_cluster(self):
        cluster_left, cluster_right = self.split_list_records()
        self.matcher.left_data.df['match_cluster_id'] = cluster_left
        self.matcher.right_data.df['match_cluster_id'] = cluster_right

    def split_list_records(self):
        part = len(self.matcher.left_data.df['id_left'])
        return self.clusters[:part], self.clusters[part:]

from scipy.cluster.hierarchy import linkage, fcluster
class HierarchicalClustering(Cluster):

    def __init__(self,
                 threshold,
                 method = 'complete',
                 metric = 'cosine',
                 criterion = 'distance'):
        self.method = method
        """single, centroid, complete, average"""
        self.metric = metric
        """‘cosine, euclidean, hamming, jaccard,..."""
        self.criterion = criterion
        """The criterion to use in forming flat clusters."""
        self.thresold = threshold

    def clustering(self):
        linkage_matrix = linkage(self.matcher.similarity_matrix, method=self.method, metric=self.metric)
        self.clusters = fcluster(linkage_matrix, t=self.thresold, criterion=self.criterion)
        self.add_cluster()

from sklearn.cluster import KMeans
class KMeansClustering(Cluster):

    def __init__(self, n_clusters):
        self.n_clusters = n_clusters

    def clustering(self):
        kmeans = KMeans(n_clusters=self.n_clusters)
        kmeans.fit(self.matcher.similarity_matrix)
        self.clusters = kmeans.labels_
        self.add_cluster()

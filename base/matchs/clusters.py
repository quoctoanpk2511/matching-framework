import abc


class Cluster:

    def __init__(self):
        super().__init__()

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def clustering(self):
        """

        Returns:

        """

    def add_cluster(self):
        cluster_left, cluster_right = self.split_list()
        self.matcher.left_data.df['Cluster'] = cluster_left
        self.matcher.right_data.df['Cluster'] = cluster_right

    def split_list(self):
        part = len(self.matcher.left_data.df['id_left'])
        return self.clusters[:part], self.clusters[part:]

from scipy.cluster.hierarchy import linkage, fcluster
class HierarchicalClustering(Cluster):

    def __init__(self, method, metric):
        super().__init__()
        self.method = method
        """single, centroid, complete, average"""
        self.metric = metric
        """‘cosine, euclidean, hamming, jaccard,..."""

    def linking(self):
        linkage_matrix = linkage(self.matcher.similarity_matrix, method=self.method, metric=self.metric)
        return linkage_matrix

    def clustering(self):
        linkage_matrix = self.linking()
        self.clusters = fcluster(linkage_matrix, t=0.35, criterion='distance')
        self.add_cluster()

from sklearn.cluster import KMeans
class KMeansClustering(Cluster):

    def clustering(self):
        kmeans = KMeans(n_clusters=11)
        kmeans.fit(self.matcher.similarity_matrix)
        self.clusters = kmeans.labels_
        self.add_cluster()

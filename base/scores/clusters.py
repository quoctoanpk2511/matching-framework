import abc


class Clustering:

    def add_matcher(self, matcher):
        """
                Add the match object on the Clustering.

                Args:
                    matcher: base.match.matchers.Matcher

                Returns: None

                """
        self.matcher = matcher
        """The matcher object"""

    @abc.abstractmethod
    def analyze(self):
        """
        Analyze data using Cluster Analysis.
        """

    def add_cluster(self):
        """
        Adding cluster results to two matcher's dataset
        """
        cluster_left, cluster_right = self.split_list_records()
        self.matcher.left_data.df['match_cluster_id'] = cluster_left
        self.matcher.right_data.df['match_cluster_id'] = cluster_right

    def split_list_records(self):
        part = len(self.matcher.left_data.df['id_left'])
        return self.matcher.clusters[:part], self.matcher.clusters[part:]

from scipy.cluster.hierarchy import linkage, fcluster
class HierarchicalClustering(Clustering):

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

    def analyze(self):
        linkage_matrix = linkage(self.matcher.similarity_matrix, method=self.method, metric=self.metric)
        self.matcher.clusters = fcluster(linkage_matrix, t=self.thresold, criterion=self.criterion)
        self.add_cluster()

from sklearn.cluster import KMeans
class KMeansClustering(Clustering):

    def __init__(self, n_clusters):
        self.n_clusters = n_clusters

    def analyze(self):
        kmeans = KMeans(n_clusters=self.n_clusters)
        kmeans.fit(self.matcher.similarity_matrix)
        self.matcher.clusters = kmeans.labels_
        self.add_cluster()

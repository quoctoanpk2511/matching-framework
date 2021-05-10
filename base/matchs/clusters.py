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
        cluster_left, cluster_right = self.split_list()
        self.matcher.left_data.df['Cluster'] = cluster_left
        self.matcher.right_data.df['Cluster'] = cluster_right

    def split_list(self):
        part = len(self.matcher.left_data.df['id_left'])
        return self.clusters[:part], self.clusters[part:]

from scipy.cluster.hierarchy import linkage, fcluster
class HierarchicalClustering(Cluster):

    def linking(self, method, metric):
        linkage_matrix = linkage(self.matcher.similarity_matrix, method=method, metric=metric)
        return linkage_matrix

    def clustering(self):
        linkage_matrix = self.linking('complete', 'cosine')
        self.clusters = fcluster(linkage_matrix, t=0.35, criterion='distance')
        self.add_cluster()

import abc


class Cluster:

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def clustering(self):
        """

        Returns:

        """

from scipy.cluster.hierarchy import linkage, fcluster
class HierarchicalClustering(Cluster):

    def linking(self, method, metric):
        linkage_matrix = linkage(self.matcher.similarity_matrix, method=method, metric=metric)
        return linkage_matrix

    def clustering(self):
        linkage_matrix = self.linking('complete', 'cosine')
        clusters = fcluster(linkage_matrix, t=0.35, criterion='distance')
        self.add_cluster(clusters)

    def add_cluster(self, clusters):
        cluster_left, cluster_right = self.split_list(clusters)
        self.matcher.data_left['Cluster'] = cluster_left
        self.matcher.data_right['Cluster'] = cluster_right

    def split_list(self, clusters):
        part = len(self.matcher.data_left['id_left'])
        return clusters[:part], clusters[part:]




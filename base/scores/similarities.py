import abc
import numpy as np

class SimilarityScorer:
    """
    Abstract class for compute the similarity of the entities.
    """

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def distance_score(self):
        """
        Compute similarity.

        Returns:
        -------
        similarity_matrix : dict
            An arary with shape of input array
        """

    def score(self):
        """
        Get each data by for loop and call distance_score(),
        save results to matcher after calling merge_matrix_with_weight_of_features().

        Returns: None
        """
        similarity_dict = {}
        for feature, vector_matrix in self.matcher.vectorizer.vectorize().items():
            similarity_dict[feature] = self.distance_score(vector_matrix)
        self.matcher.similarity_matrix = self.merge_matrix_with_weight_of_features(similarity_dict)

    def merge_matrix_with_weight_of_features(self, similarity_dict):
        """
        Merge matrix into one with its weight.

        Args:
            similarity_dict: dict

        Returns:
        -------
        similarity_matrix: array
            Similarity matrix of entities.
        """
        shape = self.matcher.get_count_entity()
        similarity_matrix = np.zeros((shape, shape))
        for feature, distance in similarity_dict.items():
            similarity_matrix += similarity_dict[feature] * self.matcher.join_features[feature]
        return similarity_matrix


from sklearn.metrics.pairwise import cosine_similarity
class Cosine_Similarity(SimilarityScorer):

    def distance_score(self, vector_matrix):
        """
        Compute cosine similarity.
        """
        return cosine_similarity(vector_matrix)

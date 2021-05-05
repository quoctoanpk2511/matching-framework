import abc
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Similarity:
    """
    Abstract class for score similarity.
    """

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def score(self):
        """

        Returns:

        """

class Cosine_Similarity(Similarity):

    def score(self, vector_dict, feature_weight_dict):
        """

        Returns:

        """

        similarity_dict = {}
        for feature, term_matrix in vector_dict.items():
            distance = cosine_similarity(term_matrix)
            similarity_dict[feature] = distance
        similarity_matrix = self.merge_matrix_with_weight_of_features(similarity_dict, feature_weight_dict)
        self.matcher.similarity_matrix = similarity_matrix

    def merge_matrix_with_weight_of_features(self, similarity_dict, feature_weight_dict):
        shape = self.matcher.get_count_entity()
        similarity_matrix = np.zeros((shape, shape))
        for feature, distance in similarity_dict.items():
            similarity_matrix += similarity_dict[feature] * feature_weight_dict[feature]
        return similarity_matrix

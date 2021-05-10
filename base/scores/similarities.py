import abc
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityScorer:
    """
    Abstract class for score similarity.
    """

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def distance_score(self):
        """

        Returns: Dict

        """

    def score(self):
        """

        Returns: None

        """
        similarity_dict = self.distance_score()
        self.merge_matrix_with_weight_of_features(similarity_dict)

    def merge_matrix_with_weight_of_features(self, similarity_dict):
        """

        Args:
            similarity_dict: Dict

        Returns: None

        """
        shape = self.matcher.get_count_entity()
        similarity_matrix = np.zeros((shape, shape))
        for feature, distance in similarity_dict.items():
            similarity_matrix += similarity_dict[feature] * self.matcher.join_features[feature]
        self.matcher.similarity_matrix = similarity_matrix

class Cosine_Similarity(SimilarityScorer):

    def distance_score(self):
        """

        Returns: Dict

        """
        similarity_dict = {}
        for feature, term_matrix in self.matcher.vectorizer.vectorize().items():
            distance = cosine_similarity(term_matrix)
            similarity_dict[feature] = distance
        return similarity_dict

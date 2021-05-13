from pandas import DataFrame
from base.preprocess.tokenizers import Tokenizer, TitleTokenizer, PriceTokenizer


class Dataset():
    """
    Class representing a dataset.
    """

    def __init__(self):
        """

        Args:
            df: DataFrame
        """

        self.df = DataFrame()
        """Dataframe contain a dataset has been read by Reader"""

    def get_list_features(self):
        """
        Method to get list of features from Dataframe.

        Returns: List
        """
        return self.df.columns.values

    def entities(self):
        """
        Method to get list of entities from Dataframe

        Returns: List
        """

        list_of_entities = []
        for row in self.df[self.get_list_features()].iterrows():
            entity = row[1]
            list_of_entities.append(dict(entity))
        return list_of_entities

    # def initiate_list_of_records(self, records, ids):
    #     for col in self.df.columns[records]:
    #         for id in ids:


class MappingFeature:

    def __init__(self):
        """

        Args:
            join_features: Dict
            feature_left: List
            feature_right: List
        """
        self.join_features = []
        """
        A List stores the feature objects.
        This represents the mapping of features from feature_left and feature_right.
        """

        self.left_features = []
        """A list of dataset1's features is used for matching."""

        self.right_features = []
        """A list of dataset2's features is used for matching."""

class Feature:

    def __init__(self, value, weight,
                 tokenizer = Tokenizer()):
        """

        """
        self.value = value
        self.weight = weight
        self.tokenizer = tokenizer

    def __hash__(self):
        return hash((self.value, self.weight))

class Title(Feature):

    def __init__(self, value, weight):
        super().__init__(value=value, weight=weight)
        self.tokenizer = TitleTokenizer()

class Price(Feature):

    def __init__(self, value, weight):
        super().__init__(value=value, weight=weight)
        self.tokenizer = PriceTokenizer()

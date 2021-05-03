from base.preprocess.features import DataMapping
from base.structures.data import Dataset1, MappingFeature, Dataset2
from base.preprocess.tokenizers import Tokenizer
from base.scores.vectorizers import Vectorizer

class Matcher():

    def __init__(self,
                 data_preprocessor = DataMapping(),
                 tokenizer = Tokenizer(),
                 vectorizer = Vectorizer(),):
        self.data_preprocessor = data_preprocessor
        self.tokenizer = tokenizer
        self.vectorizer = vectorizer

    def add_data(self,
                 data_left,
                 data_right,
                 mapping_features: MappingFeature,
                 id_left = None,
                 id_right = None):
        """
        Adding data to Matcher.

        Args:
            data_left:
            data_right:
            mapping_features:
            id_left:
            id_right:

        Returns:

        """
        self.data_left = data_left.copy()
        self.data_right = data_right.copy()
        self.join_features = mapping_features.join_features
        self.features_left = mapping_features.features_left
        self.features_right = mapping_features.features_right
        self.id_left = id_left
        self.id_right = id_right

        self.data_preprocessor.matcher(self)

    def initiate_match_record(self):
        self.records_left = []
        cols = self.features_left.copy()
        cols.append('id_left')
        for feature in self.features_left:
            dataframe_left = self.data_left[cols]
            feature_dict = {}
            for row in dataframe_left.iterrows():
                entity = row[1]
                entity_id = entity['id_left']
                entity_dict = entity[feature]
                feature_dict[entity_id] = entity_dict
            self.records_left.append(feature_dict)
        print(self.records_left)

        self.records_right = []
        cols = self.features_right.copy()
        cols.append('id_right')
        for feature in self.features_right:
            dataframe_right = self.data_right[cols]
            feature_dict = {}
            for row in dataframe_right.iterrows():
                entity = row[1]
                entity_id = entity['id_right']
                entity_dict = entity[feature]
                feature_dict[entity_id] = entity_dict
            self.records_right.append(feature_dict)
        print(self.records_right)

        self.records_join = {}
        for i in range(0, len(self.records_left)):
            join_record = {}
            join_record.update(self.records_left[i])
            join_record.update(self.records_right[i])
            self.records_join[self.join_features[i]] = join_record
            # print(self.join_features[i])
        print(self.records_join)

    def match(self):
        self.data_preprocessor.mapping()
        self.initiate_match_record()
        self.vectorizer.add_data(self)
        self.vectorizer.vectorize()
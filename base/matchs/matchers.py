from base.preprocess.data_preprocessor import DataPreprocessor
from base.structures.data import Dataset, MappingFeature
from base.scores.vectorizers import Vectorizer
from base.scores.similarities import SimilarityScorer
from base.matchs.clusters import Cluster

class Matcher():

    def __init__(self,
                 data_preprocessor = DataPreprocessor(),
                 vectorizer = Vectorizer(),
                 similarity = SimilarityScorer(),
                 cluster = Cluster(), ):
        self.data_preprocessor = data_preprocessor
        self.vectorizer = vectorizer
        self.similarity = similarity
        self.cluster = cluster

    def add_data(self,
                 left_data: Dataset,
                 right_data: Dataset,
                 mapping_features: MappingFeature,
                 id_left = None,
                 id_right = None):
        """
        Adding data to Matcher.

        Args:
            left_data:
            right_data:
            mapping_features:
            id_left:
            id_right:

        Returns:

        """
        self.left_data = left_data
        self.right_data = right_data
        self.join_features = mapping_features.join_features
        self.features_left = mapping_features.left_features
        self.features_right = mapping_features.right_features
        self.id_left = id_left
        self.id_right = id_right

    def initiate_match_record(self):
        self.records_left = []
        cols = self.features_left.copy()
        cols.append('id_left')
        for feature in self.features_left:
            dataframe_left = self.left_data.df[cols]
            feature_dict = {}
            for row in dataframe_left.iterrows():
                entity = row[1]
                entity_id = entity['id_left']
                entity_dict = entity[feature]
                feature_dict[entity_id] = entity_dict
            self.records_left.append(feature_dict)

        self.records_right = []
        cols = self.features_right.copy()
        cols.append('id_right')
        for feature in self.features_right:
            dataframe_right = self.right_data.df[cols]
            feature_dict = {}
            for row in dataframe_right.iterrows():
                entity = row[1]
                entity_id = entity['id_right']
                entity_dict = entity[feature]
                feature_dict[entity_id] = entity_dict
            self.records_right.append(feature_dict)

        self.records_join = {}
        for i in range(0, len(self.join_features)):
            join_record = {}
            join_record.update(self.records_left[i])
            join_record.update(self.records_right[i])
            self.records_join[self.join_features[i]] = join_record

    def get_list_id_record_join(self):
        list_id_records_join = list(self.left_data.df['id_left'])
        list_id_records_join.extend(list(self.right_data.df['id_right']))
        return list_id_records_join

    def get_count_entity(self):
        return len(self.left_data.df) + len(self.right_data.df)

    def match(self):
        self.data_preprocessor.matcher(self)
        self.data_preprocessor.id_preprocess()
        self.initiate_match_record()
        self.vectorizer.matcher(self)
        self.similarity.matcher(self)
        self.similarity.score()
        self.cluster.matcher(self)
        self.cluster.clustering()

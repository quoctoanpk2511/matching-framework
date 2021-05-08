from base.preprocess.data_preprocessor import DataPreprocessor
from base.structures.data import Dataset, MappingFeature
from base.preprocess.tokenizers import Tokenizer
from base.scores.vectorizers import Vectorizer
from base.scores.similarities import Similarity
from base.matchs.clusters import Cluster

class Matcher():

    def __init__(self,
                 data_preprocessor = DataPreprocessor(),
                 tokenizer = Tokenizer(),
                 vectorizer = Vectorizer(),
                 similarity = Similarity(),
                 cluster = Cluster(), ):
        self.data_preprocessor = data_preprocessor
        self.tokenizer = tokenizer
        self.vectorizer = vectorizer
        self.similarity = similarity
        self.cluster = cluster

    def add_data(self,
                 data_left: Dataset,
                 data_right: Dataset,
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
        self.data_left = data_left
        self.data_right = data_right
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
            dataframe_left = self.data_left.df[cols]
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
            dataframe_right = self.data_right.df[cols]
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
            self.records_join[list(self.join_features)[i]] = join_record

    def initiate_list_id_record_join(self):
        self.id_records_join = list(self.data_left.df['id_left'])
        self.id_records_join.extend(list(self.data_right.df['id_right']))

    def get_count_entity(self):
        return len(self.data_left.df) + len(self.data_right.df)

    def match(self):
        self.data_preprocessor.id_preprocess()
        self.initiate_match_record()
        self.initiate_list_id_record_join()
        self.vectorizer.matcher(self)
        self.similarity.matcher(self)
        self.similarity.score(self.vectorizer.vectorize(), self.join_features)
        self.cluster.matcher(self)
        self.cluster.clustering()

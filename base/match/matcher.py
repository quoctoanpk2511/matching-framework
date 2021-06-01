from base.preprocess.data_preprocessor import DataPreprocessor
from base.structures.data import Dataset, MappingFeature
from base.scores.vectorizers import Vectorizer
from base.scores.similarities import SimilarityScorer
from base.scores.clusters import Cluster

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
                 mapping_features: MappingFeature):
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

    def get_list_id_record_join(self):
        list_id_records_join = list(self.left_data.df['id_left'])
        list_id_records_join.extend(list(self.right_data.df['id_right']))
        return list_id_records_join

    def get_count_entity(self):
        return len(self.left_data.df) + len(self.right_data.df)

    def get_records_by_fields(self, dataset: Dataset, features: list, id_side):
        fields = features.copy()
        fields.append(id_side)
        list_records = []
        for field in fields:
            records = {}
            for row in dataset.df[fields].iterrows():
                row_data = row[1]
                record_id = row_data[id_side]
                record = row_data[field]
                records[record_id] = record
            list_records.append(records)
        return list_records

    def save_results(self):
        self.results = Dataset()
        self.results.df['id'] = self.get_list_id_record_join()
        for feature, records in self.records_join.items():
            self.results.df[feature.field_name] = list(records.values())
        self.results.df['cluster'] = self.clusters
        self.results.df = self.results.df.sort_values(by=['cluster'], ascending=True)

    def add_matcher(self):
        self.data_preprocessor.add_matcher(self)
        self.vectorizer.add_matcher(self)
        self.similarity.add_matcher(self)
        self.cluster.add_matcher(self)

    def match(self):
        self.add_matcher()
        self.data_preprocessor.data_preprocess()
        self.vectorizer.vectorize()
        self.similarity.score()
        self.cluster.clustering()
        self.save_results()

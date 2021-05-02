from base.preprocess.features import DataMapping
from base.structures.data import Dataset1, MappingFeature

class Matcher():

    def __init__(self,
                 data_preprocessor = DataMapping(),):
        self.data_preprocessor = data_preprocessor

    def add_data(self,
                 data_left,
                 data_right,
                 mapping_features: MappingFeature,
                 id_left = None,
                 id_right = None):
        self.data_left = data_left
        self.data_right = data_right
        self.features_left = mapping_features.features_left
        self.features_right = mapping_features.features_right
        self.id_left = id_left
        self.id_right = id_right

        self.data_preprocessor.matcher(self)

    def match(self):
        self.data_preprocessor.mapping()

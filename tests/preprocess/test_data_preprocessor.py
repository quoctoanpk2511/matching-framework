import unittest
from base.structures.data import Feature, MappingFeature
from base.utils.readers import CSVReader
from base.preprocess.data_preprocessor import DefaultDataPreprocessor
from base.matchs.matchers import Matcher

import environ
env = environ.Env()
environ.Env.read_env(env_file='../../.env')


class TestDefaultDataPreprocessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.reader1 = CSVReader('../data/left_students.csv')
        cls.reader2 = CSVReader('../data/right_students.csv')

        cls.dataset1 = cls.reader1.read()
        cls.dataset2 = cls.reader2.read()

        cls.mapping_features = MappingFeature()
        cls.mapping_features.join_features = [Feature(value='Name', weight=1)]
        cls.mapping_features.left_features = ['Name']
        cls.mapping_features.right_features = ['StdName']

        cls.data_preprocessor = DefaultDataPreprocessor()

        cls.matcher = Matcher(data_preprocessor=cls.data_preprocessor)
        cls.matcher.add_data(cls.dataset1, cls.dataset2, cls.mapping_features)
        cls.matcher.data_preprocessor.matcher(cls.matcher)
        cls.matcher.data_preprocessor.data_preprocess()

        # cls.data_preprocessor.matcher(cls.matcher)
        # cls.data_preprocessor.data_preprocess()

    def test_drop_record_with_none_value_in_feature(self):
        self.assertEqual(len(self.matcher.right_data.df), 4)


if __name__ == '__main__':
    unittest.main()

import unittest
from base.structures.data import Dataset
from base.utils.readers import Reader
from base.utils.readers import CSVReader, MySQLReader

import environ
env = environ.Env()
environ.Env.read_env(env_file='../../.env')


class TestCSVReader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.reader1 = CSVReader('../data/left_students.csv')
        cls.reader2 = CSVReader('../data/right_students.csv')

        cls.dataset1 = cls.reader1.read()
        cls.dataset2 = cls.reader2.read()

    def test_implements_readers_interface_of_reader1(self):
        self.assertIsInstance(self.reader1, Reader)

    def test_implements_readers_interface_of_reader2(self):
        self.assertIsInstance(self.reader2, Reader)

    def test_dataset1_is_created(self):
        self.assertIsInstance(self.dataset1, Dataset)

    def test_dataset2_is_created(self):
        self.assertIsInstance(self.dataset2, Dataset)

    def test_number_of_records_in_dataset1(self):
        self.assertEqual(len(self.dataset1.df), 4)

    def test_number_of_records_in_dataset2(self):
        self.assertEqual(len(self.dataset2.df), 5)


class TestMySQLReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        query1 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 1 AND cluster_id < 11"
        cls.mysql1 = MySQLReader(env('DATABASE_HOST'),
                            env('DATABASE_USER'),
                            env('DATABASE_PASSWORD'),
                            env('DATABASE_NAME'),
                            query1)
        cls.dataset1 = cls.mysql1.read()
        query2 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 0 AND cluster_id < 11"
        cls.mysql2 = MySQLReader(env('DATABASE_HOST'),
                            env('DATABASE_USER'),
                            env('DATABASE_PASSWORD'),
                            env('DATABASE_NAME'),
                            query2)
        cls.dataset2 = cls.mysql2.read()

    def test_implements_readers_interface_of_reader1(self):
        self.assertIsInstance(self.mysql1, Reader)

    def test_implements_readers_interface_of_reader2(self):
        self.assertIsInstance(self.mysql2, Reader)

    def test_dataset1_is_created(self):
        self.assertIsInstance(self.dataset1, Dataset)

    def test_dataset2_is_created(self):
        self.assertIsInstance(self.dataset2, Dataset)

    def test_number_of_records_in_dataset1(self):
        self.assertEqual(len(self.dataset1.df), 106)

    def test_number_of_records_in_dataset2(self):
        self.assertEqual(len(self.dataset2.df), 105)


if __name__ == '__main__':
    unittest.main()

import abc
import pandas as pd
from base.structures.data import (
    Dataset,
)


class Reader:
    """
    Abstract class for reading data in dataset format.
    """

    @abc.abstractmethod
    def read(self):
        """
        Returns: Dataset
        """
        return


class CSVReader(Reader):
    """
    Class reader for read data from csv file.
    """

    def __init__(self, csv_file):
        """

        Args:
            csv_file: String
        """
        self.csv_file = csv_file
        """Name of csv file that contains a dataset"""

    def read(self):
        df = pd.read_csv(self.csv_file, na_values='NaN', keep_default_na=False)
        dataset = Dataset()
        dataset.df = df
        return dataset


import MySQLdb
class MySQLReader(Reader):
    """
    Class reader for read data from MySQL database.
    """

    def __init__(self, db_host, db_user, db_passwd, db_name):
        """

        Args:
            db_host: String
            db_user: String
            db_passwd: String
            db_name: String
        """
        self.db_host = db_host
        """Database host name to connect"""
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name

    @staticmethod
    def connect(self):
        """
        Method for create a connection to the MySQL database.
        """
        con = MySQLdb.connect(
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_passwd,
            db=self.db_name)
        return con

    def read(self, query, con):
        df = pd.read_sql(query, con=con)
        dataset = Dataset()
        dataset.df = df
        return dataset

from abc import ABC, abstractmethod
import pandas as pd
from base.structures.data import (
    Dataset,
)


class Reader(ABC):
    """
    Abstract class for reading data in dataset format.
    """

    @abstractmethod
    def __init__(self):
        """

        Args:
            dataset: Dataset
        """
        super().__init__()
        self.dataset = Dataset()

    @abstractmethod
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
        super().__init__()
        self.csv_file = csv_file
        """Name of csv file that contains a dataset"""

    def read(self):
        self.dataset.df = pd.read_csv(self.csv_file, na_values='NaN', keep_default_na=False)
        return self.dataset


import MySQLdb
class MySQLReader(Reader):
    """
    Class reader for read data from MySQL database.
    """

    def __init__(self, db_host, db_user, db_passwd, db_name, sql):
        """

        Args:
            db_host: String
            db_user: String
            db_passwd: String
            db_name: String
        """
        super().__init__()
        self.db_host = db_host
        """Database host name to connect"""
        self.db_user = db_user
        """Database user name to connect"""
        self.db_passwd = db_passwd
        """Database password to connect"""
        self.db_name = db_name
        """Database name to connect"""
        self.sql = sql
        """Query to select data from MySQL database"""
        self.connect()

    def connect(self):
        """
        Method for create a connection to the MySQL database.
        """
        self.con = MySQLdb.connect(
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_passwd,
            db=self.db_name)

    def read(self):
        self.dataset.df = pd.read_sql(sql=self.sql, con=self.con)
        return self.dataset

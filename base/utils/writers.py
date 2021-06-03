import abc
import sqlalchemy
from base.structures.data import (
    Dataset,
)

class Writer():
    """
    Abstract class for writing data.
    """

    @abc.abstractmethod
    def __init__(self, dataset=Dataset()):
        """

        Args:
            dataset: Dataset
        """
        self.dataset = dataset

    @abc.abstractmethod
    def write(self):
        """
        Method to write data
        """

class CSVWriter(Writer):
    """
    Class writer for write dataset to csv file.
    """

    def __init__(self, csv_file, dataset):
        """

        Args:
            csv_file: String
        """
        super(CSVWriter, self).__init__(dataset=dataset)
        self.csv_file = csv_file
        """Name of csv file to writing the dataset"""

    def write(self):
        self.dataset.df.to_csv(self.csv_file, encoding='utf-8', index=False)


import MySQLdb
class MySQLWriter(Writer):
    """
        Class writer for write dataset to MySQL database.
    """

    def __init__(self, db_host, db_user, db_passwd, db_name, dataset):
        """

        Args:
            db_host: String
            db_user: String
            db_passwd: String
            db_name: String
        """
        super(MySQLWriter, self).__init__(dataset=dataset)
        self.db_host = db_host
        """Database host name to connect"""
        self.db_user = db_user
        """Database user name to connect"""
        self.db_passwd = db_passwd
        """Database password to connect"""
        self.db_name = db_name
        """Database name to connect"""
        self.connect()

    def connect(self):
        """
        Method for create an engine to connect to the MySQL database.
        """
        self.con = sqlalchemy.create_engine("mysql://{user}:{pw}@{host}/{db}"
				.format(host=self.db_host, db=self.db_name, user=self.db_user, pw=self.db_passwd))

    def insert(self, table_name):
        self.dataset.df[self.dataset.df.columns.difference(['id_left', 'id_right'])].to_sql(table_name, con=self.con, if_exists='append', index=False)

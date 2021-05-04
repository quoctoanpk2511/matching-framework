import abc
import pandas as pd
from base.structures.data import (
    Dataset,
    Data,
    Document,
    Dataset1,
    Entity,
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
    Reader for csv file.
    """

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read1(self, **kwargs):
        columns = []
        for key, value in kwargs.items():
            columns.append(value)
        data = pd.read_csv(self.csv_file)
        df = pd.DataFrame(data, columns=columns)
        return df

    def read2(self):
        data = Dataset()
        df = pd.read_csv(self.csv_file)
        data.items = tuple(tuple(row) for row in df.values)
        data.features = df.columns.values
        return data

    # def read3(self):
    #     data = Dataset()
    #     df = pd.read_csv(self.csv_file, na_values='NaN', keep_default_na=False)
    #     for column in df.columns.values:
    #         data.items[column] = df[column].values
    #     return data

    # def read(self):
    #     """
    #     Read csv to Dataset()
    #     """
    #     dataset = Dataset()
    #     df = pd.read_csv(self.csv_file, na_values='NaN', keep_default_na=False)
    #     for column in df.columns.values:
    #         data = Data()
    #         for index in df.index:
    #             data.documents[index] = Document(df[column][index])
    #         dataset.datas[column] = data
    #     return dataset

    def readtoDataset1(self):
        """
        Read csv to Dataset()
        """
        dataset = Dataset1()
        df = pd.read_csv(self.csv_file, na_values='NaN', keep_default_na=False)
        for entity in df.to_dict('records'):
            enti = Entity()
            # dataset.entities.append(Entity(entity))
            enti.entity = entity
            dataset.entities.append(entity)
        return dataset

    def read(self):
        df = pd.read_csv(self.csv_file, na_values='NaN', keep_default_na=False)
        return df


import MySQLdb
class MySQLReader(Reader):

    def __init__(self, db_host, db_user, db_passwd, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name

    def connect(self):
        con = MySQLdb.connect(
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_passwd,
            db=self.db_name)
        return con

    def read(self, query, con):
        df = pd.read_sql(query, con=con)
        return df

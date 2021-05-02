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

    def __init__(self, corpus_file):
        self.corpus_file = corpus_file

    def read1(self, **kwargs):
        columns = []
        for key, value in kwargs.items():
            columns.append(value)
        data = pd.read_csv(self.corpus_file)
        df = pd.DataFrame(data, columns=columns)
        return df

    def read2(self):
        data = Dataset()
        df = pd.read_csv(self.corpus_file)
        data.items = tuple(tuple(row) for row in df.values)
        data.features = df.columns.values
        return data

    # def read3(self):
    #     data = Dataset()
    #     df = pd.read_csv(self.corpus_file, na_values='NaN', keep_default_na=False)
    #     for column in df.columns.values:
    #         data.items[column] = df[column].values
    #     return data

    def read(self):
        """
        Read csv to Dataset()
        """
        dataset = Dataset()
        df = pd.read_csv(self.corpus_file, na_values='NaN', keep_default_na=False)
        for column in df.columns.values:
            data = Data()
            for index in df.index:
                data.documents[index] = Document(df[column][index])
            dataset.datas[column] = data
        return dataset

    def readtoDataset1(self):
        """
        Read csv to Dataset()
        """
        dataset = Dataset1()
        df = pd.read_csv(self.corpus_file, na_values='NaN', keep_default_na=False)
        for entity in df.to_dict('records'):
            enti = Entity()
            # dataset.entities.append(Entity(entity))
            enti.entity = entity
            dataset.entities.append(entity)
        return dataset

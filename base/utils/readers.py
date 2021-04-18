import abc
import pandas as pd
import csv

from base.structures.data import Dataset, Item

class Reader:
    """
    Abstract class for reading data in dataset format.
    """

    @abc.abstractmethod
    def read(self):
        return

class CSVReader(Reader):
    """
    Reader for csv file.
    """

    def __init__(self, corpus_file):
        self.corpus_file = corpus_file

    def read(self, **kwargs):
        dataset = Dataset()

        with open(self.corpus_file, encoding='utf-8') as file:
            # reader = csv.reader(file)
            reader = csv.DictReader(file)
            for row in reader:
                item = Item()
                # for feature in row:
                #
                #     item.documents[feature] =
                #     dataset.items[feature] = item
                # print(row, "-", row[0], "-", type(row))
                # docid, title, abstract, a, b = row
                # print(title)
                # item = Item()
                # item.documents = row
                print(row)
                dataset.items[row]
                dataset.items.update(row)
                # print(item)
            # item = Item((row[0], row[1:]) for row in reader)
            # print(item.documents)

        return dataset

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

    def read3(self):
        data = Dataset()
        df = pd.read_csv(self.corpus_file, na_values='NaN', keep_default_na=False)
        for column in df.columns.values:
            data.items[column] = df[column].values
        return data

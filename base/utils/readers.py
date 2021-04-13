import abc
import pandas as pd
import csv

from base.structures.data import Dataset, Document

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

    def read(self):
        dataset = Dataset()

        with open(self.corpus_file, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                document = Document()
                # document.parts['abstract'] = Part(row[1])
                dataset.documents[row[0]] = document

        return dataset

# reader1 = CSVReader('pricerunner_aggregate.csv')
# data1 = reader1.read()
# print(list(data1.documents.items())[1])

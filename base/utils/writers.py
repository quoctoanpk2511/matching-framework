import abc
import pandas as pd
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
        Returns: Dataset
        """
        return

class CSVWriter(Writer):
    """
    Class reader for read data from csv file.
    """

    def __init__(self, csv_file, dataset=None):
        """

        Args:
            csv_file: String
        """
        super(CSVWriter, self).__init__(dataset=dataset)
        self.csv_file = csv_file
        """Name of csv file to writing the dataset"""

    def write(self):
        self.dataset.df.to_csv(self.csv_file, encoding='utf-8', index=False)

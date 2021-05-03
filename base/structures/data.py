from collections import OrderedDict


class Dataset:
    """
    Class representing a group of items.

    :type datas: dict
    :type features: list
    """

    def __init__(self):

        self.datas = OrderedDict()
        """
        datas the dataset consists of.
        """
        self.features = []
        """
        features of dataset.
        """


    def __len__(self):
        """
        the length (size) of a dataset equals to the number of features it has
        """
        return len(self.datas)

    def __iter__(self):
        """
        when iterating through the dataset iterate through each features
        """
        for data_id, data in self.datas.items():
            yield data

    def __contains__(self, item):
        return item in self.datas

    def set_features(self, features):
        self.features = features

    def documents(self):
        for data in self:
            for document in data:
                yield document


class Data:
    """
    Class representing a single data.

    :type documents: dict
    """
    def __init__(self):
        self.documents = OrderedDict()
        """
        documents the dataset consists of.
        """
        self.vectors = []
        """
        a document-term matrix
        """

    def __eq__(self, other):
        return self.get_size() == other.get_size()

    def __lt__(self, other):
        return self.get_size() - other.get_size() < 0

    def __iter__(self):
        """
        when iterating through the document iterate through each part
        """
        for document_id, document in self.documents.items():
            yield document

    def key_value_documents(self):
        """yields iterator for partids"""
        for document_id, document in self.documents.items():
            yield document_id, document

    def entities(self):
        for document in self.documents.values():
            for e in document.text:
                yield e


class Document:
    """
    Represent list of document in data.

    :type text: str
    :type tokens: list[Token]
    """

    def __init__(self, text, is_abstract=True):
        self.text = text
        """
        the original raw text that the part is consisted of
        """
        self.tokens = []
        """
        list of tokens derived from text by calling Splitter and Tokenizer
        """


class Token:

    def __init__(self, word, start):
        self.word = word

    def __repr__(self):
        """
        print calls to the class Token will print out the string contents of the word
        """
        return self.word

class Dataset1:
    """
    Class representing a group of items.

    :type entities: List<Dict>
    :type features: List
    """

    def __init__(self):

        self.entities = []
        """
        datas the dataset consists of.
        """
        self.features = []
        """
        features of dataset.
        """


    def __len__(self):
        """
        the length (size) of a dataset equals to the number of features it has
        """
        return len(self.entities)

    def __iter__(self):
        """
        when iterating through the dataset iterate through each features
        """
        for data in self.entities:
            yield data

    def __contains__(self, item):
        return item in self.entities


class Entity(dict):

    def __init__(self):

        self.entity = {}

class MappingFeature:

    def __init__(self):
        self.join_features = {}

        # self.id_left = id_left
        self.features_left = []
        # self.id_right = id_right
        self.features_right = []

import pandas as pd
class Dataset2(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        # use the __init__ method from DataFrame to ensure
        # that we're inheriting the correct behavior
        self.records = []
        super(Dataset2,self).__init__(*args, **kwargs)

    # this method is makes it so our methods return an instance
    # of ExtendedDataFrame, instead of a regular DataFrame
    @property
    def _constructor(self):
        return Dataset2

    # def entities(self):
    #     for entity in self.to_dict('records'):
    #         enti = Entity()
    #         # dataset.entities.append(Entity(entity))
    #         enti.entity = entity
    #         dataset.entities.append(entity)

    # def initiate_list_of_records(self, records, ids):
    #     for col in self.columns[records]:
    #         for id in ids:




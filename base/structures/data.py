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

    """

    def __init__(self):
        self.documents = OrderedDict()

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


class Document:
    """
    Represent list of document in data.

    :type text: str
    :type tokens: list[Token]
    """

    def __init__(self, text, is_abstract=True):
        self.text = text
        """the original raw text that the part is consisted of"""

        self.tokens = []
        """list of tokens derived from text by calling Splitter and Tokenizer"""


class Token:

    def __init__(self, word, start):
        self.word = word

    def __repr__(self):
        """
        print calls to the class Token will print out the string contents of the word
        """
        return self.word

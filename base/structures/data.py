from collections import OrderedDict

class Dataset:
    """
    Class representing a group of items.
    """

    def __init__(self):
        """
        items the dataset consists of, encoded as a dictionary
        """
        self.items = OrderedDict()
        # self.items = {}

    # def parts(self):
    #
    #     for document in self:
    #         for part in document:
    #             yield part

class Item:
    """
    Class representing an item.
    """

    def __init__(self):

        self.documents = OrderedDict()
        # self.atrributes = []
        # self.documents = [[]]

class Document:
    """
    Class representing a single document.
    """

    def __init__(self):
        self.parts = OrderedDict()

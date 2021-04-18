from collections import OrderedDict

# class Dataset:
#     """
#     Class representing a group of items.
#     """
#
#     def __init__(self):
#         """
#         items the dataset consists of, encoded as a dictionary
#         """
#         # self.items = OrderedDict()
#         # self.items = {}
#         self.items = ()
#         self.features = []
#
#     # def parts(self):
#     #     for document in self:
#     #         for part in document:
#     #             yield part
#
#     # def parts1(self):
#     #     for document in self:
#     #         yield document

class Item:
    """
    Class representing an item.
    """

    def __init__(self):

        # self.documents = OrderedDict()
        self.atrributes = []
        # self.documents = [[]]

class Document:
    """
    Class representing a single document.
    """

    def __init__(self, text):
        self.text = text
        self.sentences = [[]]

class MatchingData:

    def __init__(self):
        self.datas = {}
        self.tokens = {}

class Dataset:

    def __init__(self):
        self.items = {}

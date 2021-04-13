from collections import OrderedDict

class Dataset:

    def __init__(self):
        self.documents = OrderedDict()

    # def parts(self):
    #
    #     for document in self:
    #         for part in document:
    #             yield part

class Document:

    def __init__(self):
        self.parts = OrderedDict()

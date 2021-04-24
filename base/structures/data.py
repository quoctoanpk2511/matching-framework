from collections import OrderedDict

class Dataset1:
    """
    Class representing a group of items.
    """

    # def __init__(self):
    #     """
    #     items the dataset consists of, encoded as a dictionary
    #     """
    #     # self.items = OrderedDict()
    #     # self.items = {}
    #     self.items = ()
    #     self.features = []
    #
    def parts(self):
        for document in self:
            for part in document:
                yield part

    def featured_parts(self):
        for document in self:
            for part in document:
                yield part

    #
    # # def parts1(self):
    # #     for document in self:
    # #         yield document

    def __init__(self):

        self.documents = OrderedDict()
        self.features = []


    def __len__(self):
        """
        the length (size) of a dataset equals to the number of documents it has
        """
        return len(self.documents)

    def __iter__(self):
        """
        when iterating through the dataset iterate through each document
        """
        for doc_id, document in self.documents.items():
            yield document

    def __contains__(self, item):
        return item in self.documents

    def set_features(self, features):
        self.features = features

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

    def __init__(self):
        self.parts = OrderedDict()
        """
        parts the document consists of, encoded as a dictionary
        where the key (string) is the id of the part
        and the value is an instance of Part
        """

    def __eq__(self, other):
        return self.get_size() == other.get_size()

    def __lt__(self, other):
        return self.get_size() - other.get_size() < 0

    def __iter__(self):
        """
        when iterating through the document iterate through each part
        """
        for part_id, part in self.parts.items():
            yield part

class Part:
    """
    Represent chunks of text grouped in the document that for some reason belong together.
    Each part hold a reference to the annotations for that chunk of text.

    :type text: str
    :type sentences_: list[str]
    :type sentences: list[list[Token]]
    :type annotations: list[Entity]
    :type predicted_annotations: list[Entity]
    :type is_abstract: bool
    """

    def __init__(self, text, is_abstract=True):
        self.text = text
        """the original raw text that the part is consisted of"""

        self.sentences_ = []
        """the text sentences previous tokenization"""

        self.sentences = [[]]
        """
        a list sentences where each sentence is a list of tokens
        derived from text by calling Splitter and Tokenizer
        """

        self.annotations = []
        """the entity of the chunk of text as populated by a call to Annotator"""

        self.predicted_annotations = []
        """
        a list of predicted entities as populated by a call to form_predicted_annotations()
        this represent the prediction on a mention label rather then on a token level
        """

        # TODO
        # warnings.warn('"annotations" (and "predicted_annotations") are meant to be "entities". This and related attributes will soon be renamed')

        self.relations = []
        """
        a list of relations that represent a connection between 2 annotations e.g. mutation mention and protein,
        where the mutation occurs inside
        """

        self.predicted_relations = []
        """a list of predicted relations as populated by a call to form_predicted_relations()"""

        self.edges = []
        """a list of possible relations between any two entities in the part"""

        self.is_abstract = is_abstract
        """whether the part is the abstract of the paper"""

        # TODO this may be too relna-specific
        self.sentence_parse_trees = []
        """the parse trees for each sentence stored as a string."""

class Token:

    def __init__(self, word, start):
        self.word = word
        """string value of the token, usually a single word"""
        self.start = start
        """start offset of the token in the original text"""
        self.end = self.start + len(self.word)
        """end offset of the token in the original text"""
        self.original_labels = None
        """the original labels for the token as assigned by some implementation of Labeler"""
        self.predicted_labels = None
        """the predicted labels for the token as assigned by some learning algorightm"""
        # self.features = FeatureDictionary()
        """
        a dictionary of features for the token
        each feature is represented as a key value pair:
        * [string], [string] pair denotes the feature "[string]=[string]"
        * [string], [float] pair denotes the feature "[string]:[float] where the [float] is a weight"
        """

    def __repr__(self):
        """
        print calls to the class Token will print out the string contents of the word
        """
        return self.word

    def __eq__(self, other):
        """
        consider two tokens equal if and only if their token words and start
        offsets coincide.
        :type other: nalaf.structures.data.Token
        :return bool:
        """
        if hasattr(other, 'word') and hasattr(other, 'start'):
            if self.word == other.word and self.start == other.start:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        """
        :type other: nalaf.structures.data.Token
        :return bool:
        """
        return not self.__eq__(other)

class MatchingData:

    def __init__(self):
        self.datas = {}
        self.tokens = {}

class Dataset:

    def __init__(self):
        self.items = {}

import abc
import nltk

from base.structures.data import (
    Dataset,
    Token,
    Dataset1,
    MappingFeature,
    Dataset2,
)


class Tokenizer:
    """
    Abstract class for splitting and tokenizing raw text.
    """

    # @abc.abstractmethod
    # def tokenize_string(self, string):
    #     return

    @abc.abstractmethod
    def tokenize(self):
        """

        Returns: None

        """


class GenericTokenizer(Tokenizer):

    def __init__(self, splitter):
        self.splitter = splitter
        "A function that takes a string as input and returns a list/iterator of tokenized string items"

    def tokenize_string(self, string):
        return self.splitter(string)

    def tokenize(self, dataset: Dataset):
        for document in dataset.documents():
            document.tokens = []
            for token_word in self.tokenize_string(document.text):
                document.tokens.append(token_word)


NLTK_TOKENIZER = GenericTokenizer(nltk.tokenize.word_tokenize)


class SimpleTokenizer(Tokenizer):

    def tokenize_string(self, string):
        str = string
        return str.lower().split()

    def tokenize(self, dataset):
        for document in dataset.documents():
            document.tokens = []
            for token_word in self.tokenize_string(document.text):
                document.tokens.append(token_word)


class StemTokenizer(Tokenizer):

    def tokenize(self, text, lang):

        stemmer = nltk.stem.snowball.SnowballStemmer(language=lang)
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        stems = [stemmer.stem(t) for t in tokens]
        return stems


# class CustomTokenizer(Tokenizer):
#
#     def __init__(self, split_func):
#         self.split_func = split_func
#
#     def tokenize_string(self, text):
#         return self.split_func(text)
#
#     def tokenize(self, data: MatchingData):
#
#         for k, v in data.datas.items():
#             list_token = []
#             for text in v:
#                 tokens = self.tokenize_string(text)
#                 list_token.append(tokens)
#             data.tokens[k] = list_token
#         return data


class CustomTokenizer(Tokenizer):

    def tokenize(self, text):
        tokens = [word.lower() for word in text.split(' ')]
        return tokens

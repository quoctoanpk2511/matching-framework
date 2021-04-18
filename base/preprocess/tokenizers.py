import abc
from typing import Dict, List

import nltk

from base.structures.data import Dataset, MatchingData


class Tokenizer:
    """
    Abstract class for tokenizing data.
    """

    @abc.abstractmethod
    def tokenize_string(self, string):
        return

    @abc.abstractmethod
    def tokenize(self, dataset):
        return

class GenericTokenizer(Tokenizer):

    def __init__(self, split_func):
        self.split_func = split_func

    def tokenize_string(self, text):
        return self.split_func(text)

    def tokenize(self, dataset):
        corup = []
        for text in dataset.items:
            tokens = self.tokenize_string(text)
            corup.append(tokens)
        return corup

class StemTokenizer(Tokenizer):

    def __init__(self):
        super().__init__()

    def tokenize(self, text, lang):
        stemmer = nltk.stem.snowball.SnowballStemmer(language=lang)
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        stems = [stemmer.stem(t) for t in tokens]
        return stems

class CustomTokenizer(Tokenizer):

    def __init__(self, split_func):
        self.split_func = split_func

    def tokenize_string(self, text):
        return self.split_func(text)

    def tokenize(self, data: MatchingData):

        for k, v in data.datas.items():
            list_token = []
            for text in v:
                tokens = self.tokenize_string(text)
                list_token.append(tokens)
            data.tokens[k] = list_token
        return data


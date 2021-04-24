import abc
from typing import Dict, List

import nltk

from base.structures.data import Dataset, MatchingData, Token, Dataset1


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

class CustomTokenizer1(Tokenizer):

    def __init__(self, string_splitter_fun):
        self.string_splitter_fun = string_splitter_fun
        "A function that takes a string as input and returns a list/iterator of tokenized string items"

    def tokenize_string(self, string):
        return self.string_splitter_fun(string)

    def tokenize(self, dataset: Dataset1):
        """

        """
        for part in dataset.parts():
            so_far = 0
            part.sentences = []
            for index, sentence_ in enumerate(part.sentences_):
                part.sentences.append([])

                for token_word in self.tokenize_string(sentence_):
                    token_start = part.text.find(token_word, so_far)
                    so_far = token_start + len(token_word)
                    part.sentences[index].append(Token(token_word, token_start))

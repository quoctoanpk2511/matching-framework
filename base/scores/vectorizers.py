import abc
from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer,
)
from base.structures.data import (
    Dataset
)


class Vectorizer:
    """
       Abstract class for convert a collection of raw documents to a matrix of TF-IDF features.
    """

    @abc.abstractmethod
    def vectorize(self, dataset):
        return


class FreqVectorizer(Vectorizer):

    def vectorize_string(self, dataset):
        count_vectorizer = CountVectorizer()
        return count_vectorizer.fit_transform(list(dataset.datas.values()))

    def vectorize(self, dataset: Dataset):
        count_vectorizer = CountVectorizer()
        for data in dataset.datas.values():
            data.tfidf_matrix = count_vectorizer.fit_transform(list[data.documents.values()])



class TfidfVectorizer(Vectorizer):

    def __init__(self, stop_words=None):
        super.__init__(stop_words=stop_words)

    def vectorizing(self):
        pass

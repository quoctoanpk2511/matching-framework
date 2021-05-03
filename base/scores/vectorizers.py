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

    def add_data(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def vectorize(self):
        """

        Returns: None

        """


class FreqVectorizer(Vectorizer):

    def vectorize_string(self, dataset):
        count_vectorizer = CountVectorizer()
        return count_vectorizer.fit_transform(list(dataset.datas.values()))

    def vectorize(self, dataset: Dataset):
        count_vectorizer = CountVectorizer()
        for data in dataset.datas.values():
            data.tfidf_matrix = count_vectorizer.fit_transform(list[data.documents.values()])


from sklearn.feature_extraction.text import TfidfVectorizer
from base.preprocess.tokenizers import CustomTokenizer
class Tf_IdfVectorizer(Vectorizer):

    def vectorize(self):
        for feature, records in self.matcher.records_join.items():
            token_list_by_dict = {}
            tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 3), tokenizer=self.matcher.tokenizer.tokenize)
            tfidf_matrix = tfidf_vectorizer.fit_transform(list(records.values()))
            print(tfidf_vectorizer.get_feature_names())
            print(tfidf_matrix)

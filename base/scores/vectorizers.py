import abc
import re
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

    def matcher(self, matcher):
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
class Tf_IdfVectorizer(Vectorizer):

    def vectorize(self):
        vector_dict = {}
        for feature, records in self.matcher.records_join.items():
            tfidf_vectorizer = TfidfVectorizer(max_df=0.7, min_df=0.01, ngram_range=(1, 3), stop_words=self.matcher.data_preprocessor.stopwords, tokenizer=self.matcher.tokenizer.tokenize)
            tfidf_matrix = tfidf_vectorizer.fit_transform(self.nomalize_data(list(records.values())))
            vector_dict[feature] = tfidf_matrix
        return vector_dict

    def nomalize_data(self, records):
        list_record = []
        for record in records:
            list_record.append(re.sub('(?<=\d) (?=gb)', '', record))
        return list_record

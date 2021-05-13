import abc


class Vectorizer:
    """
       Abstract class for convert a collection of raw documents to a matrix of TF-IDF features.
    """

    def __init__(self,
                 max_df=1,
                 min_df=1,
                 ngram_range=(1, 1)):
        self.max_df = max_df
        self.min_df = min_df
        self.ngram_range = ngram_range

    def matcher(self, matcher):
        self.matcher = matcher

    @abc.abstractmethod
    def vectorized_matrix(self):
        """
        Convert list of data to a matrix of features.

        Returns:
        -------
        vectorized_matrix: array
            A matrix after vectorize.
        """

    def vectorize(self):
        """
        Get each data by for loop and call vectorized_matrix()

        Returns:
        -------
        vectorized_dict: dict
            A dictionary with feature as key and vectorized_matrix as value.
        """
        vectorized_dict = {}
        for feature, records in self.matcher.records_join.items():
            vectorized_dict[feature] = self.vecotrized_matrix(feature, records)
        return vectorized_dict


from sklearn.feature_extraction.text import CountVectorizer
class COUNTVectorizer(Vectorizer):

    def vecotrized_matrix(self, feature, records):
        vectorizer = CountVectorizer(max_df=self.max_df,
                                           min_df=self.min_df,
                                           ngram_range=self.ngram_range,
                                           stop_words=self.matcher.data_preprocessor.stopwords,
                                           tokenizer=feature.tokenizer.tokenize_record)
        return vectorizer.fit_transform(feature.tokenizer.normalize((list(records.values()))))


from sklearn.feature_extraction.text import TfidfVectorizer
class TFIDFVectorizer(Vectorizer):

    def vecotrized_matrix(self, feature, records):
        vectorizer = TfidfVectorizer(max_df=self.max_df,
                                           min_df=self.min_df,
                                           ngram_range=self.ngram_range,
                                           stop_words=self.matcher.data_preprocessor.stopwords,
                                           tokenizer=feature.tokenizer.tokenize_record)
        return vectorizer.fit_transform(feature.tokenizer.normalize(list(records.values())))

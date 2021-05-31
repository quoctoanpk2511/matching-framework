import abc


class Tokenizer():
    """
    Abstract class for splitting and tokenizing raw text.
    """

    def add_matcher(self, matcher):
        """
        Add the match object on the Tokenizer.

        Args:
            matcher: base.matchs.matchers.Matcher

        Returns: None

        """
        self.matcher = matcher
        """The matcher object"""

    @abc.abstractmethod
    def tokenize_record(self, text):
        """
        An abstract method to tokenize string.

        Args:
            string: String

        Returns: List

        """
        return

    def tokenize(self):
        """
        Method to tokenize all feature of dataset by calling tokenize_string() function.
        Returns a dictionary with feature as key and list tokens as value.

        Returns: Dict

        """
        dict_of_list_token = {}
        for feature, records in self.matcher.records_join.items():
            list_token = []
            for record in records.values():
                list_token.append(self.tokenize_string(record))
            dict_of_list_token[feature] = list_token
        return dict_of_list_token

    @abc.abstractmethod
    def normalize_record(self, record):
        """

        Returns:

        """
        return record

    def normalize(self, records):
        nomalized_records = []
        for record in records:
            nomalized_records.append(self.normalize_record(record))
        return nomalized_records


class GenericTokenizer(Tokenizer):
    """
    A generic tokenizer.
    """

    def __init__(self, splitter):
        self.splitter = splitter
        """Splitter function"""

    def tokenize_record(self, text):
        """
        A function that takes a string as input and returns a list/iterator of tokenized string items

        Args:
            text: String

        Returns: List

        """
        return self.splitter(text)


from nltk import word_tokenize
NLTK_TOKENIZER = GenericTokenizer(word_tokenize)


class DefaultTokenizer(Tokenizer):
    """
    Class default for tokenizer
    """

    def tokenize_record(self, record):
        tokens = [word.lower() for word in record.split(' ')]
        return tokens


from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
class StemTokenizer(Tokenizer):
    """
    A class for tokenizer and stemmer.
    """

    def __init__(self, language):
        self.language = language
        """Language used for stemmer"""

    def tokenize_string(self, text):
        stemmer = SnowballStemmer(language=self.language)
        tokens = [word for word in word_tokenize(text)]
        stems = [stemmer.stem(t) for t in tokens]
        return stems

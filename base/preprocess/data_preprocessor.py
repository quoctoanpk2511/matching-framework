import abc


class DataPreprocessor:
    """
    Abstract class to process and standardize data of the dataset.
    """

    def __init__(self,
                 stopwords = []):
        self.stopwords = stopwords

    def matcher(self, matcher):
        """
        Add the match object on the Dataprocess.

        Args:
            matcher: base.matchs.matchers.Matcher

        Returns: None

        """
        self.matcher = matcher
        """The matcher object"""

    @abc.abstractmethod
    def data_preprocess(self):
        """

        Returns: None

        """

    def id_preprocess(self):
        """
        Method to process the IDs of two dataset.

        Returns: None

        """
        if not self.matcher.id_left:
            self.add_id(self.matcher.left_data.df, "left")
        else:
            self.matcher.left_data.df['id_left'] = self.matcher.left_data.df[self.matcher.id_left]
        if not self.matcher.id_right:
            self.add_id(self.matcher.right_data.df, "right")
        else:
            self.matcher.right_data.df['id_right'] = self.matcher.right_data.df[self.matcher.id_right]

    def add_id(self, df, side):
        """
        Static method of DataPreprocessor to add new IDs into the dataset if it is not has IDs

        Args:
            dataset: DataFrame
            side: String

        Returns: None

        """
        id_side = "id_" + side
        id_list = ["{}_{}".format(i, side) for i in range(0, len(df))]
        df[id_side] = id_list


class DefaultDataPreprocessor(DataPreprocessor):

    def data_preprocess(self):
        """

        Returns:

        """



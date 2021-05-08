class DataPreprocessor:
    """
    Class to process and standardize the IDs of the dataset.
    """

    def matcher(self, matcher):
        """
        Add the match object on the Dataprocess.

        Args:
            matcher: base.matchs.matchers.Matcher

        Returns: None

        """
        self.matcher = matcher
        """The matcher object"""

    def id_preprocess(self):
        """
        Method to process the IDs of two dataset.

        Returns: None

        """

        if not self.matcher.id_left:
            self.add_id(self.matcher.data_left.df, "left")
        else:
            self.matcher.data_left.df['id_left'] = self.matcher.data_left.df[self.matcher.id_left]
        if not self.matcher.id_right:
            self.add_id(self.matcher.data_right.df, "right")
        else:
            self.matcher.data_right.df['id_right'] = self.matcher.data_right.df[self.matcher.id_right]

    @staticmethod
    def add_id(dataframe, side):
        """
        Static method of DataPreprocessor to add new IDs into the dataset if it is not has IDs

        Args:
            dataset: DataFrame
            side: String

        Returns: None

        """
        id_side = "id_" + side
        id_list = ["{}_{}".format(i, side) for i in range(0, len(dataframe))]
        dataframe[id_side] = id_list

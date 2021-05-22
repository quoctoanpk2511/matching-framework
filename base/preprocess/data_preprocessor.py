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

    def initiate_match_record(self):
        self.matcher.records_left = []
        cols = self.matcher.features_left.copy()
        cols.append('id_left')
        for feature in self.matcher.features_left:
            dataframe_left = self.matcher.left_data.df[cols]
            feature_dict = {}
            for row in dataframe_left.iterrows():
                entity = row[1]
                entity_id = entity['id_left']
                entity_dict = entity[feature]
                feature_dict[entity_id] = entity_dict
            self.matcher.records_left.append(feature_dict)

        self.matcher.records_right = []
        cols = self.matcher.features_right.copy()
        cols.append('id_right')
        for feature in self.matcher.features_right:
            dataframe_right = self.matcher.right_data.df[cols]
            feature_dict = {}
            for row in dataframe_right.iterrows():
                entity = row[1]
                entity_id = entity['id_right']
                entity_dict = entity[feature]
                feature_dict[entity_id] = entity_dict
            self.matcher.records_right.append(feature_dict)

        self.matcher.records_join = {}
        for i in range(0, len(self.matcher.join_features)):
            join_record = {}
            join_record.update(self.matcher.records_left[i])
            join_record.update(self.matcher.records_right[i])
            self.matcher.records_join[self.matcher.join_features[i]] = join_record


class DefaultDataPreprocessor(DataPreprocessor):

    def data_preprocess(self):
        """

        Returns:

        """



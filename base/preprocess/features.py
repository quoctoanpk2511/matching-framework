import abc
from base.structures.data import (
    Dataset,
    Token,
    Dataset1,
    MappingFeature,
    Dataset2,
)


# class DataMapping:
#     """
#     Abstract class for mapping single or many dataset.
#     """
#
#     @abc.abstractmethod
#     def mapping(self):
#         """
#         Returns: None
#         """


class DataMapping:

    def add_data(self, matcher):
        self.matcher = matcher

    def mapping(self):

        if not self.matcher.id_left:
            self.add_id(self.matcher.data_left, "left")
        else:
            self.matcher.data_left['id_left'] = self.matcher.data_left[self.matcher.id_left]
        if not self.matcher.id_right:
            self.add_id(self.matcher.data_right, "right")
        else:
            self.matcher.data_right['id_right'] = self.matcher.data_right[self.matcher.id_right]

    @staticmethod
    def add_id(dataset: Dataset2, side):
        id_side = "id_" + side
        id_list = ["{}_{}".format(i, side) for i in range(0, len(dataset))]
        dataset[id_side] = id_list

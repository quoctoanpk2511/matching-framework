import abc
import pandas as pd

class PreProcessorABC():

    __metaclass__ = abc.ABCMeta

    # def __init__(self):
    #     pass

    def inputReader(self):
        pass

    def removeSpecialChar(self, input):

        self.input = input

    def process(self, df, row_labels, template):
        # df = pd.DataFrame(input, columns=row_labels)
        # pd.read_csv
        for row in df.itertuples():
            pass

data = '{"1":{"name": "Bob", "languages": ["Python", "Java"]}, "2":{"name": "Bob2", "languages": "Python"}}'
df = pd.read_json(data)
# df = pd.DataFrame(data)
print(type(df))
print(df)


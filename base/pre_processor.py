####### test csv
from base.utils.readers import CSVReader
from base.structures.data import (
    Dataset,
    Data,
    Document,
)
from base.preprocess.tokenizers import GenericTokenizer
from nltk.tokenize import word_tokenize

# reader1 = CSVReader('./data/pricerunner_aggregate.csv')
reader1 = CSVReader('./data/students.csv')

# from base.structures.data import Dataset1
# print("read")
# test3 = reader1.read()
# for k,v  in test3.documents.items():
#     for v1 in v:
#         print(v1)

# print("parts")
# for part in (test3.parts()):
#     print(part)

# print("test key value")
# for k, v in test3.documents.items():
#     print(k, v)
#     for v1 in v:
#         print(v1)

# print("test parts")
# for part in test3.parts():
#     print(part)

# print("test document")
# for document in test3.documents.items():
#     if document.
#     print(document)

# print("test features")
# test3.set_features(['Name'])
# print(test3.features)
#
# print("test 4")
# test4 = Dataset()
# for k, v in test3.datas.items():
#     for feature in test3.features:
#         if k == feature:
#             test4.datas[k] = v

# print("Doc")
# for doc in test3:
#     print(doc.parts)

# print("test 5")
# test5 = Dataset()
# for k, v in test3.datas.items():
#     for feature in test3.features:
#         if k == feature:
#             test5.datas[k] = v
# for doc in test5:
#     # print(doc)
#     # print(doc.parts)
#     for part in doc:
#         print(part.text)

# print("part test 5")
# for document in test5.documents():
#     print(document.text)

from base.preprocess.tokenizers import GenericTokenizer, NLTK_TOKENIZER, SimpleTokenizer
# test nltk tokenizer : done
# tokens1 = NLTK_TOKENIZER
# tokens1.tokenize(test5)
# for document in test5.documents():
#     print(document.tokens)

# test simple tokenizer : done
# tokens2 = SimpleTokenizer()
# tokens2.tokenize(test5)
# for document in test5.documents():
#     print(document.tokens)

# test vectorizer chua xong
from base.scores.vectorizers import FreqVectorizer
freq = FreqVectorizer()
# freq.vectorize(test5)
# for data in test5:
#     print(data.documents.values())
#     print(data.vectors)

# for data in test5.datas.values():
#     for doc in list(data.documents.values()):
#         print(doc.text)

# for data in test5:
#     for doc_id, doc in data.key_value_documents():
#         print(doc.text)

# for data in test5:
#     for e in data.entities():
#         print(e)

#test Dataset1
from base.structures.data import Dataset1, MappingFeature
from base.preprocess.tokenizers import CustomTokenizer
from base.preprocess.features import DataMapping
from base.matchs.matchers import Matcher

dataset1 = CSVReader('./data/students.csv').readtoDataset1()

dataset2 = CSVReader('./data/students1.csv').readtoDataset1()
# for e in dataset2.entities:
#     for k, v in e.items():
#         print(k, v)

mappingfeatures = MappingFeature()
mappingfeatures.features = ['Name']
mappingfeatures.features_left = ['Name']
mappingfeatures.features_right = ['StdName']

# token = CustomTokenizer().tokenize(dataset1, mappingfeatures)

# dmap = DataMapping()
# m = Matcher(dmap)
# m.add_data(dataset1, dataset2, mappingfeatures)
# print(m.id_left, m.id_right)
# m.match()
# for data in m.data_left:
#     print(data)

from base.structures.data import Dataset2
import pandas as pd
dataset3 = pd.read_csv('./data/students.csv')
dataset4 = pd.read_csv('./data/students1.csv')

dmap = DataMapping()
m = Matcher(dmap)
m.add_data(dataset3, dataset4, mappingfeatures)
m.match()
print(m.data_left)
print(m.data_right)

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
print("read")
test3 = reader1.read()
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

print("test features")
test3.set_features(['Name'])
print(test3.features)

print("test 4")
test4 = Dataset()
for k, v in test3.datas.items():
    for feature in test3.features:
        if k == feature:
            test4.datas[k] = v

# print("Doc")
# for doc in test3:
#     print(doc.parts)

print("test 5")
test5 = Dataset()
for k, v in test3.datas.items():
    for feature in test3.features:
        if k == feature:
            test5.datas[k] = v
# for doc in test5:
#     # print(doc)
#     # print(doc.parts)
#     for part in doc:
#         print(part.text)

# print("part test 5")
# for document in test5.documents():
#     print(document.text)

from base.preprocess.tokenizers import GenericTokenizer, NLTK_TOKENIZER, SimpleTokenizer
tokens1 = NLTK_TOKENIZER
tokens1.tokenize(test5)
for document in test5.documents():
    print(document.tokens)

tokens2 = SimpleTokenizer()
tokens2.tokenize(test5)
for document in test5.documents():
    print(document.tokens)

from base.scores.vectorizers import FreqVectorizer


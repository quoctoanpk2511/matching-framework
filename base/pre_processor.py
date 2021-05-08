####### test csv
from base.utils.readers import CSVReader
from base.structures.data import (
    Dataset,
    MappingFeature,
)
from base.preprocess.tokenizers import GenericTokenizer
from nltk.tokenize import word_tokenize

# reader1 = CSVReader('./data/pricerunner_aggregate.csv')
# reader1 = CSVReader('./data/students.csv')

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

from base.preprocess.tokenizers import GenericTokenizer, NLTK_TOKENIZER
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
# freq = FreqVectorizer()
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
from base.preprocess.tokenizers import DefaultTokenizer
from base.preprocess.data_preprocessor import DataPreprocessor
from base.matchs.matchers import Matcher

dataset1 = CSVReader('./data/students.csv').read()

dataset2 = CSVReader('./data/students1.csv').read()
# for e in dataset2.entities:
#     for k, v in e.items():
#         print(k, v)

# mappingfeatures = MappingFeature()
# mappingfeatures.join_features = {'JoinName':0.5, 'JoinCity':0.5}
# mappingfeatures.features_left = ['Name', 'City']
# mappingfeatures.features_right = ['StdName', 'StdCity']

# token = CustomTokenizer().tokenize(dataset1, mappingfeatures)

# dmap = DataMapping()
# m = Matcher(dmap)
# m.add_data(dataset1, dataset2, mappingfeatures)
# print(m.id_left, m.id_right)
# m.match()
# for data in m.data_left:
#     print(data)

from base.utils.readers import CSVReader, MySQLReader
from base.scores.vectorizers import Tf_IdfVectorizer
from base.preprocess.tokenizers import DefaultTokenizer, GenericTokenizer, NLTK_TOKENIZER
from base.scores.similarities import Cosine_Similarity
from base.matchs.clusters import HierarchicalClustering
import pandas as pd

#read from csv
# dataset3 = pd.read_csv('./data/students.csv')
# dataset4 = pd.read_csv('./data/students1.csv')

#read from sql
import environ
import MySQLdb
# Reading .env file
env = environ.Env()
environ.Env.read_env()

# Connect to SQL Server
# mydb = MySQLdb.connect(
#     host=env('DATABASE_HOST'),
#     user=env('DATABASE_USER'),
#     passwd=env('DATABASE_PASSWORD'),
#     db=env('DATABASE_NAME'))
query1 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND cluster_id < 11"
mysql = MySQLReader(env('DATABASE_HOST'),
                    env('DATABASE_USER'),
                    env('DATABASE_PASSWORD'),
                    env('DATABASE_NAME'),
                    query1)
# con = mysql.connect()
dataset3 = mysql.read()

query2 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND cluster_id < 5"
mysql = MySQLReader(env('DATABASE_HOST'),
                    env('DATABASE_USER'),
                    env('DATABASE_PASSWORD'),
                    env('DATABASE_NAME'),
                    query2)
dataset4 = mysql.read()

# print(dataset3.shape)
# print(dataset4.shape)

mappingfeatures = MappingFeature()
mappingfeatures.join_features = {'product_title':1}
mappingfeatures.features_left = ['product_title']
mappingfeatures.features_right = ['product_title']

dmap = DataPreprocessor()
t = DefaultTokenizer()
tfidf = Tf_IdfVectorizer()
sim = Cosine_Similarity()
cluster = HierarchicalClustering()

m = Matcher(data_preprocessor=dmap, tokenizer=t, vectorizer=tfidf, similarity=sim, cluster=cluster)
m.add_data(dataset3, dataset4, mappingfeatures)
m.match()

# print(m.data_left)
# print(m.data_right)
from fuzzymatcher.record import RecordToMatch, Record

# m.right_records = {}
# cols = m.features_right.copy()
# cols.append("id_right")
# df = m.data_right[cols]
# for r in df.iterrows():
#     row = r[1]
#     fields_dict = dict(row[m.features_right])
#     this_id = row["id_right"]
#     rec = Record(fields_dict, this_id, m)
#     m.right_records[this_id] = rec
# print(m.right_records)



# from sklearn.feature_extraction.text import TfidfVectorizer
# for feature, records in m.records_join.items():
#     token_list_by_dict = {}
#     tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 3), tokenizer=CustomTokenizer.tokenize)
#     tfidf_matrix = tfidf_vectorizer.fit_transform(list(records.values()))
#     print(tfidf_vectorizer.get_feature_names())
#     print(tfidf_matrix)
# m.vectorizer.vectorize()
print(m.data_left.df)
print(m.data_right.df)

# m.tokenizer = NLTK_TOKENIZER
# m.tokenizer.matcher(m)
# # print(m.tokenizer.tokenize())
#
# from base.preprocess.tokenizers import StemTokenizer
# m.tokenizer = StemTokenizer("english")
# m.tokenizer.matcher(m)
# print(m.tokenizer.tokenize())

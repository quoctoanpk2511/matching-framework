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

####### test csv
from base.utils.readers import CSVReader
from base.structures.data import Dataset, Document, Item, MatchingData, DataRaw
from base.preprocess.tokenizers import GenericTokenizer, CustomTokenizer
from nltk.tokenize import word_tokenize

# reader1 = CSVReader('./data/pricerunner_aggregate.csv')
reader1 = CSVReader('./data/students.csv')
# data = reader1.read()
# print(data)
# data1 = reader1.read1(id='Id', name='Name', course='Course', session='Session')
# print(data1)
data = Dataset()
data2 = Item()
data = reader1.read2()
data2.atrributes = data.items
# print(data.items)
# print(data.features)
# print(data2.atrributes)
matchdata = MatchingData()
for fe in data.features:
    for i in data.items:
        matchdata.datas[fe] = i
# print(matchdata.datas)

data3 = MatchingData()
data4 = reader1.read3()
print(data4.items)
for k, v in data4.items.items():
    if k == 'Name':
        data3.datas[k] = v
print(data3.datas)
tokens = CustomTokenizer(word_tokenize)
print(tokens.tokenize(data3).tokens)


# print(list(data1.items.items()))
# for item in data1.items.items():
#     print(item[0])
#     print(type(item[0]))

# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# import time
# from sklearn.metrics.pairwise import cosine_similarity
# from  scipy.cluster import hierarchy
# from scipy.cluster.hierarchy import ward, dendrogram, linkage, fcluster
#
# stopwords = []
#
# # tokenizer
# def tokenizer(text):
#     tokens = [word.lower() for word in text.split(' ')]
#     return tokens
#
# # tfidf_vectorizer = TfidfVectorizer(max_df=0.6, max_features=20000, min_df=10, stop_words=stopwords, use_idf=True, ngram_range=(1,3), tokenizer=tokenize)
# # tfidf_vectorizer = TfidfVectorizer(max_df=0.6, max_features=20000, min_df=10, stop_words=stopwords, use_idf=False, ngram_range=(1,3), tokenizer=tokenize)
# tfidf_vectorizer = TfidfVectorizer(max_df=0.7, max_features=20000, min_df=0.01, stop_words=stopwords, ngram_range=(1,3), tokenizer=tokenize)
# start = time.time()
# tfidf_matrix = tfidf_vectorizer.fit_transform(list_title)
# print("Time: ", time.time() - start)
# print(tfidf_matrix.shape)
# # print(tfidf_matrix[0])
#
# terms = tfidf_vectorizer.get_feature_names()
# print(terms)
# dist = cosine_similarity(tfidf_matrix)
# linkage_matrix = linkage(dist, 'complete', metric='cosine') #define the linkage_matrix using single-linkage clustering pre-computed distances
# clusters = fcluster(linkage_matrix, t=0.65, criterion='distance')
# print("Len clusters: ", len(clusters))
# print(clusters)
# clus_set = list(set(clusters))
# print(clus_set)
#
# clus_list = []
# for i in range(0, len(clusters)):
#     clus_dict = {'id': list_id[i], 'old_cluster': list_old_cluster[i], 'new_cluster': clusters.item(i), 'title': list_title[i]}
#     clus_list.append(clus_dict)
# clus_list.sort(key=lambda item: item.get("new_cluster"))
# for cl in clus_list:
#     print(cl)

####### test tokenize
str = "This is an orange walks in the table"
# str2 = "This is an orange walks in the desk"
# def setup(cls):
#     cls.dataset = Dataset()
#     item = Item()
#     item.documents['p1'] = Document('This is some sample text. This is another, sample sentence with coma.')
#     item.documents['p1'].sentences_ = ['This is some sample text.', 'This is another, sample sentence with coma.']
#     # dataset = Dataset()
#     cls.dataset.items['item1'] = item
#     for part in cls.dataset.parts():
#         print(part)
# a = Dataset()
# setup(a)
# item = Item()
# item.documents['p1'] = Document('This is some sample text. This is another, sample sentence with coma.')
# item.documents['p1'].sentences_ = ['This is some sample text.', 'This is another, sample sentence with coma.']
# dataset = Dataset()
# dataset.items['item1'] = item.documents
# print(dataset.items)
# for part in dataset.parts():
#     print(part)
# for k in dataset.items.items():
#     print(k)
# print(item.documents['p1'])
# tokens = GenericTokenizer(word_tokenize)
# print(tokens.tokenize(dataset))
# print(tokens.tokenize(dataset))
# tokens = StemTokenizer()
# print(tokens.tokenize(str, 'english'))
# str = Dataset()
# str.items['p2'] = 'asdasd'
# for i in str.parts():
#     print(i)


### ok tokenize
# corpus = [
#     'first document1 document1 .',
#     'The first first first document. first',
#     'And this is the third one.',
#     'four document1 document1 ?',
#     'four document2 document2',
# ]
#
# dataset = Dataset()
# dataset.items = corpus
# print(dataset.items)
# tokens = GenericTokenizer(word_tokenize)
# print(tokens.tokenize(dataset))
# print(tokens.tokenize_string(str))
# tokens1 = StemTokenizer()
# print(tokens1.tokenize(dataset, 'english'))



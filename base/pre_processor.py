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


from base.utils.readers import CSVReader

# reader1 = CSVReader('./data/pricerunner_aggregate.csv')
reader1 = CSVReader('./data/students.csv')
data = reader1.read()
print(data)
print(data.items.items())
data1 = reader1.read1(id='Id', name='Name', course='Course', session='Session')
print(data1)
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

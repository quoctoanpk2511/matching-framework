from base.structures.data import (
    MappingFeature,
    Title,
)
from base.utils.readers import CSVReader, MySQLReader
from base.preprocess.data_preprocessor import DefaultDataPreprocessor
from base.scores.vectorizers import TFIDFVectorizer
from base.preprocess.tokenizers import DefaultTokenizer, GenericTokenizer, NLTK_TOKENIZER
from base.scores.similarities import Cosine_Similarity
from base.matchs.clusters import HierarchicalClustering
from base.matchs.matchers import Matcher

dataset1 = CSVReader('./data/students.csv').read()

dataset2 = CSVReader('./data/students1.csv').read()

#read from csv
# dataset1 = pd.read_csv('./data/students.csv')
# dataset2 = pd.read_csv('./data/students1.csv')

#read from sql
import environ
# Reading .env file
env = environ.Env()
environ.Env.read_env()

query1 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 1 AND cluster_id < 11"
mysql = MySQLReader(env('DATABASE_HOST'),
                    env('DATABASE_USER'),
                    env('DATABASE_PASSWORD'),
                    env('DATABASE_NAME'),
                    query1)
dataset1 = mysql.read()
query2 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 0 AND cluster_id < 11"
mysql = MySQLReader(env('DATABASE_HOST'),
                    env('DATABASE_USER'),
                    env('DATABASE_PASSWORD'),
                    env('DATABASE_NAME'),
                    query2)
dataset2 = mysql.read()

title = Title(value='product_title', weight=1)

mapping_features = MappingFeature()
mapping_features.join_features = [title]
mapping_features.left_features = ['product_title']
mapping_features.right_features = ['product_title']

stopwords = ['black', 'white', 'grey', 'silver', 'unlocked', 'sim', 'free', 'water', 'dust', 'resistant', 'by',
                     'gold', 'rose', 'space', 'handset', 'only', 'mobile phone', 'phone',
                     'smartphone', 'in', 'mobile', 'single', 'cm', '4g', '4.7', '5.5', '5.8']

data_preprocessor = DefaultDataPreprocessor(stopwords=stopwords)
vectorizer = TFIDFVectorizer(max_df=0.7, min_df=0.01, ngram_range=(1,3))
similarity_scorer = Cosine_Similarity()
cluster = HierarchicalClustering(threshold=0.35)
# cluster = KMeansClustering(n_clusters=11)

m = Matcher(data_preprocessor=data_preprocessor,
            # tokenizer=tokenizer,
            vectorizer=vectorizer,
            similarity=similarity_scorer,
            cluster=cluster)
m.add_data(dataset1, dataset2, mapping_features)
m.match()

print(m.left_data.df)
print(m.right_data.df)

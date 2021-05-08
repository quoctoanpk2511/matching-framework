from base.utils.readers import CSVReader, MySQLReader
from base.preprocess.data_preprocessor import DataPreprocessor
from base.preprocess.tokenizers import DefaultTokenizer, GenericTokenizer, NLTK_TOKENIZER
from base.scores.vectorizers import Tf_IdfVectorizer
from base.scores.similarities import Cosine_Similarity
from base.matchs.clusters import HierarchicalClustering
from base.matchs.matchers import Matcher
import environ

env = environ.Env()
environ.Env.read_env()

def start_match(mapping_features,
                id_left = None,
                id_right = None):
    query1 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND cluster_id < 11"
    mysql = MySQLReader(env('DATABASE_HOST'),
                        env('DATABASE_USER'),
                        env('DATABASE_PASSWORD'),
                        env('DATABASE_NAME'),
                        query1)
    dataset1 = mysql.read()
    query2 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND cluster_id < 5"
    mysql = MySQLReader(env('DATABASE_HOST'),
                        env('DATABASE_USER'),
                        env('DATABASE_PASSWORD'),
                        env('DATABASE_NAME'),
                        query2)
    dataset2 = mysql.read()

    data_preprocessor = DataPreprocessor()
    tokenizer = DefaultTokenizer()
    vectorizer = Tf_IdfVectorizer()
    similarity_scorer = Cosine_Similarity()
    cluster = HierarchicalClustering()

    m = Matcher(data_preprocessor=data_preprocessor,
                tokenizer=tokenizer,
                vectorizer=vectorizer,
                similarity=similarity_scorer,
                cluster=cluster)
    m.add_data(dataset1, dataset2, mapping_features)
    m.match()
    return m

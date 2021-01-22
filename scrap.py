# import libraries
from sqlalchemy import create_engine
import pandas as pd

import nltk
from nltk.corpus import wordnet as wn, stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
import re
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

def load_data(data_file):
    # load data from database
    engine = create_engine('sqlite:///Disaster_Response.db')
    df = pd.read_sql_table(table_name='DisasterMessages', con=engine)

    # Spliting data into inputs and outputs
    X = df['message']
    y = df.drop(['id', 'message', 'genre'], axis=1)
    y = y.astype('int')
    return X, y


def tokenize(text):
    tag_map = defaultdict(lambda: wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV

    lemma = WordNetLemmatizer()
    punctuations = "!?<>.,;'\\][)(@#$%^&*/"
    tokens_lemma = []

    # lower-casing tokens
    tokens = word_tokenize(text.lower())
    # removing punctuations
    tokens = [token for token in tokens if token not in punctuations]
    # removing stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # lemmatizing tokens
    for token, tag in pos_tag(filtered_tokens):
        tokens_lemma.append(lemma.lemmatize(token, tag_map[tag[0]]))

    return tokens_lemma


def build_model():

    model = Pipeline([
        ('tfidf', TfidfVectorizer(tokenizer=tokenize)),
        ('business_logic', MultiOutputClassifier(KNeighborsClassifier()))
    ])
    return model


def train(X, y, model):
    # splitting train into train and test batches and rearranging the ordering of their samples
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=10)

    # Training business_logic
    model.fit(X_train, y_train)

    return model


def export_model(model):
    saved_model = pickle.dump(model, 'business_logic.pyc')
    return saved_model


def run_pipeline(data_file):
    X, y = load_data(data_file)  # run ETL pipeline
    model = build_model()  # build business_logic pipeline
    model = train(X, y, model)  # train business_logic pipeline
    export_model(model)  # save business_logic

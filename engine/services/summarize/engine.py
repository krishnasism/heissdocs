import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os

from ..utils.helpers import clean_text


class SummaryEngine:
    def __init__(self):
        # initialize_nltk()
        pass

    def initialize_nltk(self):
        nltk.download()

    def summarize(self, text: str) -> list:
        sentences = sent_tokenize(text)

        stop_words = set(stopwords.words("english"))
        f = open(f"{os.path.dirname(os.path.realpath(__file__))}/stopwords.txt")
        for stops in f.read().split():
            stop_words.add(stops)

        vectorizer = TfidfVectorizer(stop_words="english")
        X = vectorizer.fit_transform(sentences)

        # Fit data into 2 clusters
        true_k = 2
        model = KMeans(n_clusters=true_k, init="k-means++", max_iter=100, n_init=1)
        model.fit(X)

        # Score each cluster
        c1 = []
        c2 = []
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        for i in range(true_k):
            for ind in order_centroids[i, :10]:
                if i == 0:
                    c1.append(terms[ind])
                else:
                    c2.append(terms[ind])

        sentence_score = {}
        sc = 1.0
        for sentence in sentences:
            sc = 1.0
            for word in c1:
                if word in sentence.lower():
                    if sc <= 0:
                        sc = 0
                    if sentence in sentence_score.keys():
                        sentence_score[sentence] += sc
                        sc = sc - 0.05
                    else:
                        sentence_score[sentence] = sc
                        sc = sc - 0.05

        sum_total = 0
        for sentence in sentences:
            if sentence in sentence_score.keys():
                sum_total += sentence_score[sentence]

        average_score = int(sum_total / len(sentence_score))

        summary = []

        for sentence in sentences:
            if (
                sentence in sentence_score.keys()
                and sentence_score[sentence] > 2.2 * average_score
            ):
                summary.append(clean_text(sentence))

        sentence_score2 = {}

        for sentence in sentences:
            sc = 1.0
            for word in c2:
                if word in sentence.lower():
                    if sc <= 0:
                        sc = 0
                    if sentence in sentence_score2.keys():
                        sentence_score2[sentence] += sc
                        sc = sc - 0.05
                    else:
                        sentence_score2[sentence] = sc
                        sc = sc - 0.05

        sum_total = 0
        for sentence in sentences:
            if sentence in sentence_score2.keys():
                sum_total += sentence_score2[sentence]

        average_score = int(sum_total / len(sentence_score2))

        for sentence in sentences:
            # Multiply with best factor - Determined 2.2 after trial & error
            if (
                sentence in sentence_score2.keys()
                and sentence_score2[sentence] > 2.2 * average_score
            ):
                summary.append(clean_text(sentence))

        return summary

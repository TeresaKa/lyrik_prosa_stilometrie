import glob
import regex as re
from collections import Counter

import pandas as pd
from scipy.stats import zscore
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


def stop_word_removal(x):
    token = x.split()
    return ' '.join([w for w in token if not w in german_stop_words])

german_stop_words = stopwords.words('german')
vect = CountVectorizer(stop_words = german_stop_words)


df = pd.read_csv('Arent_raw/arent_anthologie_gedichte.csv')
df['removedstopword']  = df['text'].apply(stop_word_removal)

Liste = []
count_vect = CountVectorizer()
for i, row in df.iterrows():
    count_vect.fit_transform(row.removedstopword.split())
    titel = str(row.Autor)+'_'+str(row.Titel)
    dic = count_vect.vocabulary_
    frequencies = list(dic.values())
    words = list(dic.keys())
    Liste.append(pd.Series(frequencies, words, name=titel))

docf = pd.DataFrame(Liste)
docf = docf.fillna(0)
docf = docf.div(docf.sum(axis=1), axis=0)
print(docf)


class Zscores:
    def __init__(self, path):
        self.path = path

    def tokenize(self, lines, pattern=re.compile(r'\p{L}+')):
        """
        :param lines: object to be tokenized, e.g. file
        :param pattern: pattern to tokenize 'lines'
        :return: lowered and tokenized string
        """
        for line in lines:
            yield from map(str.lower, pattern.findall(line))

    def wordcounts_in_file(self, file):
        """
        :param file: filename of file to be analyzed
        :return: Counter of tokenized file
        """
        with open(file, encoding='utf-8') as f:
            return Counter(self.tokenize(f))

    def word2freq(self, counts):
        """
        :param counts: a Counter from a file to be analyzed
        :return: list of each words and their frequencies
        """
        words = []
        freq = []
        for c in counts:
            words.append(c)
            freq.append(counts[c])
        return words, freq


    def create_dataframe(self, freqlist, mfw):
        """
        :param freqlist: list of pd.Series, created e.g. with create_pd_series()
        :param mfw: value of most frequent words
        :return: document-term-matrix as pd.Dataframe with zscores
        """
        df = pd.DataFrame(freqlist)
        df = df.fillna(0)

        df = df.div(df.sum(axis=1), axis=0)

        df.loc['Total_per_word'] = df.sum()
        df = df.sort_values(by='Total_per_word', axis=1, ascending=False)
        df.drop('Total_per_word', inplace=True, axis=0)

        zscores = df.apply(zscore)
        zscores.drop(zscores.columns[mfw:], inplace=True, axis=1)
        return df, zscores


def frequencies(path):
    Z = Zscores(path)
    series = Z.create_pd_series()

    mfw_values = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    #corpus = path.split('/')[2]

    for mfw in mfw_values:
        freq, zscores = Z.create_dataframe(series, mfw)
        zscores.to_csv('zscores')
        freq.to_csv('frequency')
    print(zscores)

if __name__ == "__main__":
    path = df
  #  prefix =

    frequencies(path)
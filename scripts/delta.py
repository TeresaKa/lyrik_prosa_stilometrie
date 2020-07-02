import glob
import pandas as pd
import numpy as np
from scipy.spatial import distance


class Delta:
    def __init__(self, df, unknown):
        """
        :param df: document-term-matrix with zscores
        :param unknown: specify unknown document in 'df' to be compared with remaining texts
        """
        self.df = df
        self.unknown = unknown

    def calculate_distance(self):
        """ Calculates Manhattan, Cosine and Euclidean Delta measures and returns them as pd.Series """
        series_list = []
        for index, row in self.df.iterrows():
            print(self.unknown, row)
            manhattan = distance.cityblock(row, self.df.loc[self.unknown])
            cosine = distance.cosine(row, self.df.loc[self.unknown])
            euclidean = distance.euclidean(row, self.df.loc[self.unknown])
            series_list.append(pd.Series([manhattan,cosine, euclidean,'?'], ['manhattan','cosine','euclidean', 'label'], name=index))
        return series_list

    def create_distance_df(self):
        distance_measures = self.calculate_distance()
        distance = pd.DataFrame(distance_measures)
        distance.sort_values(by=['manhattan', 'cosine', 'euclidean'], inplace=True)  # ist das nötig?
        distance = distance.round(2)
        distance.cosine = 1 - distance.cosine
        return distance

    def assign_labels(self):
        """ Compares author of 'unknown' text with authors of remaining texts.
        Assigns labels: 'same' if authors match, 'different' otherwise. """
        delta = self.create_distance_df()
        delta.name = self.unknown
        delta['genres'] = '0'
        for i, row in delta.iterrows():
            genre = i.split('_')[0]
            delta.loc[i, 'genres'] = str(genre)
            if type(delta.genres[i]) != str:
                print(i, delta.genres[i])
            if delta.genres[0] == delta.genres[i]:
                delta.loc[i, 'label'] = 'same'
            else:
                delta.loc[i, 'label'] = 'different'
        return delta


def delta_attribution(path, prefix):
    for file in glob.glob(path):
        filename = file.replace(prefix, '').replace(file[-4:], '')
        zscores = pd.read_csv(file,  index_col=[0])
        attribution = pd.DataFrame()
        for u in zscores.index:
            attribution = pd.concat([attribution, Delta(zscores, u).assign_labels()])
        print(attribution)
        attribution.to_hdf('../results/delta/delta_hauptcorpus.h5',  key='data', mode='w')


if __name__ == "__main__":
    path = '../results/delta/zscores_hauptcorpus.csv'
    prefix = '../results/delta/'

    delta_attribution(path, prefix)

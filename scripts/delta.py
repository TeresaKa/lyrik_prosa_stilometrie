import glob
import pandas as pd
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
            # manhattan = distance.cityblock(row, self.df.loc[self.unknown])
            print("row", row, "unknown",self.unknown)
            cosine = distance.cosine(row, self.df.loc[self.unknown])
            # euclidean = distance.euclidean(row, self.df.loc[self.unknown])
            series_list.append(pd.Series([cosine, '?'], ['cosine', 'label'], name=index))
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
        for i, row in delta.iterrows():
            author = i.split(',')[0]
            delta.loc[i, 'author'] = author
            if delta.author[0] == delta.author[i]:
                delta.loc[i, 'label'] = 'same'
            else:
                delta.loc[i, 'label'] = 'different'
        return delta


def delta_attribution(path, prefix):
    for file in glob.glob(path):
        filename = file.replace(prefix, '').replace(file[-3:], '')
        mfw = filename.split('_')[0]
        # corpus = filename.split('_')[2]
        print(file)
        zscores = pd.read_csv(file)
        attribution = pd.DataFrame()
        print(zscores)
        for u in zscores.index:
            attribution = pd.concat([attribution, Delta(zscores, u).assign_labels()])
        attribution.to_hdf(str(mfw) + '_delta_' + '.h5',  key='data', mode='w')


if __name__ == "__main__":
    path = '../results/zscores_lyrik.csv'
    # path='../results/10_zscore_Chinese.h5'
    prefix = 'results/'

    delta_attribution(path, prefix)

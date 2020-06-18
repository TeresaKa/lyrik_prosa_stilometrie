import pandas as pd
import os
import glob
import os
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

def mfw(path):
    ''' zählt Wordhäufigkeiten pro Segment '''
    stopword = open("de_stopwords.txt")
    stopwords = stopword.read()
    freq_list = []
    words = []
    for text in os.listdir(path):
        t = open(path + '/' + text, 'r')
        f = t.read()
        title = text.split('/')[0]
        stop = ' '.join([item for item in str(f).split() if item not in stopwords])
        c = Counter(stop.split())
        sort_vocab = {k: v for k, v in sorted(c.items(), key=lambda item: item[1],reverse=True)}
        words.append(list(sort_vocab.keys())[:1000])
    return words

def mfw_only_duplicates(list):
    dupl = set(list[0]) & set(list[1])
    return dupl

def drop_duplicates(list):
    mfw = list[0] + list[1]
    res = []
    for i in mfw:
        if i not in res:
            res.append(i)
    return res

mfw = mfw('corpora')
ohne_dupl = drop_duplicates(mfw)
nur_dupl = mfw_only_duplicates(mfw)
emotion = ['liebreich','angst', 'ängstlich', 'trauer', 'traurig', 'zornig', 'zorn', 'verachtungsvoll', 'verachtung', 'schuld', 'schuldig', 'liebe',  'geliebt', 'liebevoll', 'stolz', 'scham', 'schämen', 'überrasschung', 'überrascht', 'sorge', 'sorgenvoll', 'ekel', 'ekeln', 'angeekelt', 'neid', 'neidisch', 'neidvoll', 'glücklich', 'glück', 'freude', 'freudig', 'freuen', 'erleichterung', 'erleichtert', 'vergnügt', 'vergnügen', 'zufrieden', 'zufriedenheit', 'verzweiflung', 'verzweifelt', 'verlegenheit', 'verlegen', 'aufregung', 'aufgeregt', 'aufregen', 'spannung', 'gespannt', 'erregung', 'erregt', 'hoffen', 'hoffnung', 'befriedigt', 'langweilig', 'langeweile', 'mitgefühl', 'mitfühlen', 'enttäuscht', 'enttäuschung', 'frust', 'frustriert', 'eifersucht', 'eifersüchtig', 'wut', 'wütend', 'reue', 'schock', 'schockiert', 'zuneigung', 'verärgert', 'verärgerung', 'erwartungsvoll', 'erwartung', 'vorfreude', 'scheu', 'gelassen', 'gelassenheit', 'mut', 'mutig', 'neugierde', 'neugierig', 'depression', 'depressiv', 'niedergeschlagenheit', 'niedergeschlagen', 'lustvoll', 'lust', 'rausch', 'einfühlend', 'einfühlsam', 'euphorisch', 'euphorie', 'dankbarkeit', 'dankbar', 'hass', 'entsetzt', 'entsetzen', 'demütigung', 'demütig', 'demut', 'interesse', 'interessiert', 'einsamkeit', 'einsam', 'empörung', 'empört', 'vertrauen', 'qualvoll', 'qual', 'gleichgültigkeit', 'gleichgültig', 'fröhlichkeit', 'fröhlich', 'schadenfroh', 'schadenfreude', 'schmerz', 'melancholie', 'melancholisch', 'panik', 'panisch']
nomen = ['freude','vertrauen', 'angst','überraschung', 'trauer', 'ekel', 'wut', 'mitgefühl', 'liebe']
anf = ['\"', '»', '«']
### erkennt direkte Rede in den Dokumenten und rechnet die relative Häufigkeit 'aus'
def count_merkmale(Partition):
    häufigkeitSegment = 0
    anzahl = 0
    for text in os.listdir(Partition):
        startIndex = 0
        t = open(Partition + "/" + text, "r")
        f = t.read()
        if text.endswith(".txt"):
            anzahl += 1
            for e in nur_dupl:
                if e in f:
                    startIndex+=1
                    #startIndex =+ f.count(e) #'\"')
                print(text, e, startIndex)
        if startIndex >= 1:
            häufigkeitSegment += 1
            # print(text, häufigkeitSegment)
    rf_directSpeech = häufigkeitSegment/anzahl
    print("Anzahl der Segmente: " + str(anzahl))
    print("Wie häufig kommt das Anführungszeichen insgesamt im Segment vor: " + str(startIndex))
    print("Relative Häufigekeit (in wie vielen Segmenten kommt es vor): " + str(rf_directSpeech))
    return rf_directSpeech



def zeta_per_word(Partition):
    häufigkeitSegment = 0
    anzahl = 0
    dic = {}
    for wort in emotion:
        for text in os.listdir(Partition):
            startIndex = 0
            t = open(Partition + "/" + text, "r")
            f = t.read()
            if text.endswith(".txt"):
                anzahl += 1
                if wort in f:
                    startIndex+=1
                    #startIndex =+ f.count(e) #'\"')
                print(text, wort, startIndex)
            if startIndex >= 1:
                häufigkeitSegment += 1
                # print(text, häufigkeitSegment)
        rf_directSpeech = häufigkeitSegment/anzahl
        dic[wort] = rf_directSpeech
    return dic


### Zeta
def zeta(anteilZ, anteilV):
    zeta = anteilZ - anteilV
    return zeta
# ### Ziel
pfadV = 'segmentelyrik'
pfad = ['segmentelyrik', 'segmenteepik']
pfadZ = 'segmenteepik'
# epik = directSpeech(pfadV)
# lyrik = directSpeech(pfadZ)

# pfadV = ('C:\\Users\\pinaj\\Documents\\Uni\\DH\\Stilometrie\\Code')
lyrik = zeta_per_word(pfadV)
prosa = zeta_per_word(pfadZ)
zetas = {}
for wort in nur_dupl:
    print(zeta(lyrik[wort], prosa[wort]))

### Zeta - Aufbau

# zwei Partionen

# charakteristische Ermittlungen
    # Wortformen
    # Lemmata
    # frequencies
    # Sonderzeichen?
    # Emotionswörter?

# Häufigkeit der Merkmale ermitteln

# for i in Partition:
    # ermittel relative Häufigkeit (rf), in wie vielen Segmenten der Partition mindestens einmal?
    # für Ziel und Vergleich
    # für jedes Merkmal
    # -> df (document frequency)

# tf-idf-Score?
# X^2?
# llr?


# print("Zeta:", zeta_directSpeech(lyrik, epik))
# Rechnung (1 bis -1; 1 = Ziel charakteristisch; -1 = Vergleich charakteristisch; 0 = nicht charakteristisch)
    # Anteil / Anzahl der Segmente (je Z und V)
    # Anteil(Z) - Anteil(V) = Zeta




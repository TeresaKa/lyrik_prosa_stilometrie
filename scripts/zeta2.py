import pandas as pd
import os
import glob
import os
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

import spacy
import de_core_news_md
from spacy.lemmatizer import Lemmatizer
# nlp = de_core_news_md.load()

### Löst Anführungszeichen von Wörtern, damit sie einzeln betrachtet werden können
def replace(string, ffilter):
    for char in ffilter:
        string = string.replace(char, " ")
        string = string.replace("\"", " \" ")
    return string


### Teilt den Korpus in gleichgroße Segmente und schreibt alles klein
def segment(wordList, n):
    for i in range(0, len(wordList), n):
        datei = []
        if i + n <= len(wordList):
            for j in range(i, i+n):
                datei.append(wordList[j].encode('utf8').lower())
            if os.path.exists("segmenteepik/epik_Segment" + str(i) + ".txt"):
                txtFile = open("segmenteepik/epik_Segment" + str(i) + ".txt", "w")
                txtFile.write("")
                txtFile.close()

            txtFile = open("segmenteepik/epik_Segment" + str(i) + ".txt", "a")
            for word in datei:
                txtFile.write(word.decode('utf8') + " ")
            txtFile.close()
        else:
            pass
            # for j in range(i, len(wordList)):
            #     datei.append(wordList[j])
    return

def lemma(path):
    charFilter = ",.!;:—?-_(){}[]/\\"
    for text in os.listdir(path):
        t = open(path + '/' + text, 'r')
        f = t.read()
        lemmata = [f]
        f_lemma = []
        for i in lemmata:
            doc = nlp(i)
            result = ''
            for token in doc:
                result += token.lemma_
                result += ' '
            f_lemma.append(result)
        print(f_lemma[0], type(f_lemma[0]))
        # file = path + '/lemma_' + text
        if os.path.exists('lemma_' + text):
            txtFile = open('lemma_' + text, 'w')
            txtFile.write('')
            txtFile.close()
        txtFile = open('lemma_'+text,'a')
        for i in f_lemma:
            txtFile.write(replace(i, charFilter + ' '))
        txtFile.close()
    return
p = '../corpus/Arent/Arent_raw/'
# print("text", lemma(p))

def mfw(path):
    ''' zählt Wordhäufigkeiten pro Segment '''
    freq_list = []
    for text in os.listdir(path):
        t = open(path + '/' + text, 'r')
        f = t.read()
        title = text.split('/')[0]
        c = Counter(f.split())
        sort_vocab = {k: v for k, v in sorted(c.items(), key=lambda item: item[1],reverse=True)}
        print(sort_vocab)
        # set(a) & set(b)
    #     frequencies = list(vocab.values())
    #     words = list(vocab.keys())
    #     freq_list.append(pd.Series(frequencies, words, name=title))
    #     # print(freq_list)
    # counts = pd.DataFrame(freq_list)
    # counts = counts.fillna(0)
    # counts = counts.div(counts.sum(axis=1), axis=0)
    # # counts.loc['Total_per_word'] = counts.sum()
    # counts = counts.sort_values(by=['corpus_Arent.txt', 'corpus_German_prosa.txt'], axis=1, ascending=False)
    # counts.drop('Total_per_word', inplace=True, axis=0)
    return
print(mfw('corpora'))

### erkennt direkte Rede in den Dokumenten und rechnet die relative Häufigkeit aus
def directSpeech(Partition):
    häufigkeitSegment = 0
    anzahl = 0
    for text in os.listdir(Partition):
        t = open(Partition + "/" + text, "r")
        f = t.read()
        if text.endswith(".txt"):
            anzahl +=1
            startIndex = f.count('\"')
            if startIndex >= 1:
                häufigkeitSegment += 1
    rf_directSpeech = häufigkeitSegment/anzahl
    print("Anzahl der Segmente: " + str(anzahl))
    print("Wie häufig kommt das Anführungszeichen insgesamt im Segment vor: " + str(startIndex))
    print("Relative Häufigekeit (in wie vielen Segmenten kommt es vor): " + str(häufigkeitSegment))
    return rf_directSpeech



### Korpus-Vorbereitung

### fügt alle txt-Datein zu einer Großen zusammen. Text nicht in einer Zeile
### (funktioniert)
charFilter = ",.!;:—?-_(){}[]/\\"

def korpus_vorbereitung():
    read_files = glob.glob("../corpus/Arent/lemma/*.txt")
    path = os.path.dirname('../corpus/Arent/lemma/*.txt"')
    corpus = path.split('/')[2]
    with open("result.txt", "wb") as outfile:
        for f in read_files:
            print(f)
            with open(f, "rb") as infile:
                outfile.write(infile.read().lower())
    corpus_name = os.rename('result.txt', 'corpus_' + str(corpus) + '.txt')
    return



### zählt Wörter der txt-Datei
### (funkioniert)

# file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "r")
# data = file.read()
# words = data.split()
# print('Number of words', len(words))


### (funktioniert)
# file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', 'r')
# data = file.read()
#
# charFilter = ",.!;:—?-_(){}[]/\\"  # funktioniert
#
# data = replace(data, charFilter) # funktioniert
#
# einzelSegment = segment(data.split(), 100) # funktioniert
#
# segment(data.split(), 100) # funktioniert

# # file = open('../corpus/Arent/corpus_Arent_raw.txt', 'r', encoding='utf-8')
# file = open('corpus_German_prosa.txt','r', encoding='utf-8')
# data = file.read().casefold()
#
# charFilter = ",.!;:—?-_(){}[]/\\"
#
#
# data = replace(data, charFilter)
# print(data.split())
# segment(data.split(), 100)


# def directSpeech()
# ### Ziel
# pfadV = 'segmenteepik'
# pfadZ = 'segmente'
# epik = directSpeech(pfadV)
# lyrik = directSpeech(pfadZ)

# pfadV = ('C:\\Users\\pinaj\\Documents\\Uni\\DH\\Stilometrie\\Code')
# print(directSpeech(pfadV))




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

### Zeta
def zeta_directSpeech(anteilZ, anteilV):
    zeta = anteilZ - anteilV
    return zeta

# print("Zeta:", zeta_directSpeech(lyrik, epik))
# Rechnung (1 bis -1; 1 = Ziel charakteristisch; -1 = Vergleich charakteristisch; 0 = nicht charakteristisch)
    # Anteil / Anzahl der Segmente (je Z und V)
    # Anteil(Z) - Anteil(V) = Zeta




import pandas as pd
import os
import glob
import os



def replace(string, ffilter):
    for char in ffilter:
        string = string.replace(char, "")
        string = string.replace("\"", " \" ")
    return string


def segment(wordList, n):
    for i in range(0, len(wordList), n):
        datei = []
        if i + n <= len(wordList):
            for j in range(i, i+n):
                datei.append(wordList[j])
            if os.path.exists("segmente/Segment" + str(i) + ".txt"):
                txtFile = open("segmente/Segment" + str(i) + ".txt", "w")
                txtFile.write("")
                txtFile.close()

            txtFile = open("segmente/Segment" + str(i) + ".txt", "a")
            for word in datei:
                txtFile.write(word + " ")
            txtFile.close()
        else:
            pass
            # for j in range(i, len(wordList)):
            #     datei.append(wordList[j])
    return


# def lowerCases(input_file):
#     with open(input_file) as fileinput:
#         for line in fileinput:
#             line = line.lower()

### Korpus-Vorbereitung

### fügt alle txt-Datein zu einer Großen zusammen. Text nicht in einer Zeile

read_files = glob.glob("../corpus/Arent/Arent_raw/*.txt") #C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt")
path = os.path.dirname('../corpus/Arent/Arent_raw/*.txt') #C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt')
corpus = path.split('/')[2]
#C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/result.txt"
with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
corpus_name = os.rename('result.txt', 'corpus_' + str(corpus) + '.txt')



### zählt Wörter der txt-Datei

file = open("../corpus/Arent/corpus_Arent_raw.txt", 'r') #C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "r")
data = file.read()
words = data.split()
print('Number of words', len(words))




file = open('../corpus/Arent/corpus_Arent_raw.txt', 'r', encoding='utf-8')
data = file.read().casefold()

charFilter = ",.!;:—?-_(){}[]/\\"


data = replace(data, charFilter)
print(data.split())
segment(data.split(), 100)



### Zeta

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

# Rechnung (1 bis -1; 1 = Ziel charakteristisch; -1 = Vergleich charakteristisch; 0 = nicht charakteristisch)
    # Anteil / Anzahl der Segmente (je Z und V)
    # Anteil(Z) - Anteil(V) = Zeta

### Direkte Sprache
def directSpeech(Partition):
    häufigkeitSegment = 0
    anzahl = 0
    for text in glob.glob(Partition):
        t = open(text)
        f = t.read()
        anzahl +=1
        startIndex = f.count('\"')
        if startIndex >= 1:
            häufigkeitSegment += 1
        print(text, startIndex)
    print("Anzahl der Segmente: " + str(anzahl))
    print("Wie häufig kommt das Anführungszeichen insgesamt im Segment vor: " + str(startIndex))
    print("Relative Häufigekeit (in wie vielen Segmenten kommt es vor): " + str(häufigkeitSegment))
    return

partition = "segmente/*.txt"
directSpeech(partition)
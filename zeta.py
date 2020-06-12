import pandas as pd
import os
import glob
import os


### Löst Anführungszeichen von Wörtern, damit sie einzeln betrachtet werden können
def replace(string, ffilter):
    for char in ffilter:
        string = string.replace(char, "")
        string = string.replace("\"", " \" ")
    return string


### Teilt den Korpus in gleichgroße Segmente
def segment(wordList, n):
    for i in range(0, len(wordList), n):
        datei = []
        for j in range(i, i+n):
            datei.append(wordList[j])

        if os.path.exists("Segment"+str(i)+".txt"):
            txtFile = open("Segment"+str(i)+".txt", "w")
            txtFile.write("")
            txtFile.close()

        txtFile = open("Segment"+str(i)+".txt", "a")
        for word in datei:
            txtFile.write(word + " ")
        txtFile.close()
    return


### !!! soll Umlaute entfernen
def umlaute(Segmente):
    file = open(Segmente, 'r', encoding='utf-8').read().casefold()
    file.close()
    return


### erkennt direkte Rede in einem!!! Dokument, bei mehreren: Fehlermeldung. Glob geht auch nicht.
def directSpeech(Partition):
    häufigkeitSegment = 0
    for text in Partition:
        startIndex = text.count('\"')
        if startIndex >= 1:
            häufigkeitSegment += 1
    print(startIndex)
    return häufigkeitSegment


### Korpus-Vorbereitung

### fügt alle txt-Datein zu einer Großen zusammen. Text nicht in einer Zeile
### (funktioniert)

# read_files = glob.glob("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt")
# path = os.path.dirname('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt')
# corpus = path.split('/')[8]
# with open("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/result.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())
# corpus_name = os.rename('result.txt', 'corpus_' + str(corpus) + '.txt')



### zählt Wörter der txt-Datei
### (funkioniert)

# file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "r")
# data = file.read()
# words = data.split()
# print('Number of words', len(words))



### !!! def umlaute. Soll Umlaute entfernen
# segmenteUmlaute = glob.glob('C:\Users\pinaj\Documents\Uni\DH\Stilometrie\Code\Segmente_Arent\*.txt')
# umlaute(segmenteUmlaute)

### !!! soll Umlaute entfernen
# file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', 'r', encoding='utf-8')
# data = file.read().casefold()

### (funktioniert)
# file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', 'r')
# data = file.read()

# charFilter = ",.!;:—?-_(){}[]/\\"  # funktioniert
#
# data = replace(data, charFilter) # funktioniert
#
# einzelSegment = segment(data.split(), 100) # funktioniert
#
# segment(data.split(), 100) # funktioniert

# def directSpeech()
pfad = open(r'C:\Users\pinaj\Documents\Uni\DH\Stilometrie\Code\SegmenteArent\Segment56100.txt')
print(directSpeech(pfad))




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

# Rechnung (1 bis -1; 1 = Ziel charakteristisch; -1 = Vergleich charakteristisch; 0 = nicht charakteristisch)
    # Anteil / Anzahl der Segmente (je Z und V)
    # Anteil(Z) - Anteil(V) = Zeta




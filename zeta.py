import pandas as pd
import os
import glob
import os



### fügt alle txt-Datein zu einer Großen zusammen. Text nicht in einer Zeile

read_files = glob.glob("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt")
path = os.path.dirname('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt')
corpus = path.split('/')[8]
with open("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
corpus_name = os.rename('result.txt', 'corpus_' + str(corpus) + '.txt')




### zählt Wörter der txt-Datei

file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "rt")
data = file.read()
words = data.split()
print('Number of words', len(words))


def replace(string, ffilter):
    for char in ffilter:
        string = string.replace(char, "")
    return string


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


file = open("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt", "r")
data = file.read()

charFilter = ",.!;:—?-_\"(){}[]/\\"


data = replace(data, charFilter)


segment(data.split(), 99)
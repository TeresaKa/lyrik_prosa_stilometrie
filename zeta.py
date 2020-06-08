import pandas as pd
import os
import glob

#Pseudo-Code

### fügt alle txt-Datein zu einer großen zusammen. Text nicht in einer Zeile

read_files = glob.glob("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt")
path = os.path.dirname('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/Arent_raw/*.txt')
corpus = path.split('/')[8]
with open("C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
corpus_name = os.rename('result.txt', 'corpus_' + str(corpus) + '.txt')


### nur der String, nicht die txt-Datei

# def cutchunks(string, length):
#     return (string[0+i:length+i] for i in range(0, len(string), length))
#
# text = ('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt')
# lines = (i.strip() for i in text.splitlines())
# for line in lines:
#     for chunk in cutchunks(line, 5):
#         print(chunk)


### nach Zeile, nicht nach Wörtern

def chunks(t, n):
    for i in range(0, len(t), n):
        yield t[i:i + n]

tokens = []
with open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt') as main_file:
    for token in main_file:
        tokens.append(token)

for i, group in enumerate(chunks(tokens, n=100), start=1):
    with open('file%d.txt' % i, mode="w") as out_file:
        for line in group:
            out_file.write(token)


### zählt Wörter der txt-Datei

file = open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "rt")
data = file.read()
words = data.split()
print('Number of words', len(words))


### 3522 Datein mit der Wiederholung der ersten Zeile

# def chunks(t, n):
#     for i in range(0, len(t), n):
#          yield t[i:i + n]
#
# with open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt') as file:
#      for token in file:
#          data = file.read()
#          words = data.split()
#
# for i, group in enumerate(chunks(data, n=100)):
#     with open('file%d.txt' % i, mode="w") as out_file:
#        for line in group:
#            out_file.write(token)


### zählt alle Wörter auf (print in PyCharm, nicht gespeichert)

with open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "rt") as f:
    for line in f:
        for word in line.split():
            print(word)


### erstellt eine Datei mit dem letzten Wort

# with open('C:/Users/pinaj/Documents/Uni/DH/Stilometrie/Code/corpus_Arent_raw.txt', "rt") as f:
#     for line in f:
#         for word in line.split():
#             with open('file%d.txt', mode="w") as out_file:
#                 out_file.write(word)







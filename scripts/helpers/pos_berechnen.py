import glob
import os
import treetaggerwrapper
from collections import Counter

inpath1 = '../corpus/corpora/corpora_gesamt/corpus_epik.txt'
inpath2 = '../corpus/corpora/corpora_gesamt/corpus_lyrik.txt'

def POS(text):
    verben = []
    substantive = []
    adjektive = []
    pronomen = []
    t = open(text, 'r')
    f = t.read()
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
    tags = tagger.tag_text(f)
    tags2 = treetaggerwrapper.make_tags(tags)
    for t in tags2:
        if t.pos=='VVFIN' or t.pos=='VVINF':
            verben.append(t.lemma)
        elif t.pos=='ADJD' or t.pos=='ADJA':
            adjektive.append(t.lemma)
        elif t.pos=='NN' or t.pos=='NA':
            substantive.append(t.lemma)
        elif t.pos=='PPER' or t.pos=='PPOSS' or t.pos=='PPOSAT':
            pronomen.append(t.lemma)
    return verben, adjektive, substantive, pronomen

def wortliste(liste):
    c = Counter(liste).most_common(n=1000)
    wortliste = []
    for element in c:
        wortliste.append(element[0])
    return wortliste

def drop_duplicates(list):
    res = []
    for i in list:
        if i not in res:
            res.append(i.lower())
    return res

verben1, adjektive1, substantive1, pronomen1 = POS(inpath1)
verben2, adjektive2, substantive2, pronomen2 = POS(inpath2)

verben = drop_duplicates(wortliste(verben1) + wortliste(verben2))
adjektive = drop_duplicates(wortliste(adjektive1) + wortliste(adjektive2))
substantive = drop_duplicates(wortliste(substantive1) + wortliste(substantive2))
pronomen = drop_duplicates(wortliste(pronomen1) + wortliste(pronomen2))
print(verben,'\n', len(verben),'\n',adjektive, '\n', len(adjektive),'\n',substantive,'\n', len(substantive), '\n', pronomen, '\n', len(pronomen))
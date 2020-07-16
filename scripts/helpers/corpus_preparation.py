import glob
import os
import treetaggerwrapper


def replace(string, filter):
    ''' Entfernt Elemente in filter aus string und entfernt Anführungszeichen. '''
    for char in filter:
        string = string.replace(char, " ")
        string = string.replace("\"", " \" ")
        string = string.lower()
    return string

def lemma(inpath, outpath, charFilter):
    ''' Lemmatisiert Texte in gegebenem Ordner inpath. '''
    for text in os.listdir(inpath):
        if text.endswith('.txt'):
            f_lemma = []
            result = ''
            t = open(inpath + '/' + text, 'r')
            f = t.read()
            tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
            tags = tagger.tag_text(f)
            tags2 = treetaggerwrapper.make_tags(tags)
            print("text", text)
            for t in tags2:
                try:
                    result += t.lemma
                    result += ' '
                except:
                    pass
            f_lemma.append(result)
            if os.path.exists(outpath + text.split('_')[1]+'_'+text.split('_')[2]+'.txt'):
                txtFile = open(outpath + text.split('_')[1]+'_'+text.split('_')[2]+'.txt', 'w')
                txtFile.write('')
                txtFile.close()
            txtFile = open(outpath + text.split('_')[1]+'_'+text.split('_')[2]+'.txt', 'a')
            for i in f_lemma:
                txtFile.write(replace(i, charFilter + ' '))
            txtFile.close()
    return

charFilter = ",.!;:—?-_(){}[]/\\"
# inpath = '../corpus/autoren_corpora/autoren_lyrik/'
# outpath = '../corpus/autoren_corpora/autoren_lyrik/autoren_lyrik_lemma/autoren_lyrik_lemma_'
# print("text", lemma(inpath, outpath, charFilter))
#
def concat_corpus(path):
    ''' Fügt alle txt-Datein zu einer Großen zusammen '''
    read_files = glob.glob(path) #Arent/lemma/*.txt")
    path = os.path.dirname(path)
    corpus = path.split('/')[2]
    print(read_files)
    with open("../corpus/result.txt", "wb") as outfile:
        for f in read_files:
            print(f)
            with open(f, "rb") as infile:
                outfile.write(infile.read()) #.lower())
    corpus_name = os.rename('../corpus/result.txt', '../corpus/corpus_' + str(corpus) + '.txt')
    return corpus_name
path = "../corpus/segmente/zklein_gesamt/*.txt"
concat_corpus(path)
# tagger.tag_file_to('../corpus/German_prosa/prosa/achleitner_bergrichters.txt', '../corpus/German_prosa/prosa/achleitner_bergrichters2.txt') #evtl für gesamtes Korpus


def segment(wordList, n, outpath):
    """ Teilt den Korpus wordList in Segmente der Länge n. """
    for i in range(0, len(wordList), n):
        datei = []
        if i + n <= len(wordList):
            for j in range(i, i+n):
                datei.append(wordList[j].encode('utf8')) #.lower())

            if os.path.exists(outpath + str(i) + ".txt"):
                txtFile = open(outpath + str(i) + ".txt", "w")
                txtFile.write('')
                txtFile.close()
            txtFile = open(outpath + str(i) + ".txt", "a")
            for word in datei:
                txtFile.write(word.decode('utf8') + " ")
            txtFile.close()
        else:
            pass
    return

#
# out = '../corpus/segmente/keller_epik_500/epik'
# words = open('../corpus/autoren_corpora/keller/gesamt/corpus_keller_epik.txt', 'r')
# wordList = words.read()
# segment(wordList.split(), 500, out)

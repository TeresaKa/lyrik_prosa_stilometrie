import pandas as pd
import os
import glob
import os
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter


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




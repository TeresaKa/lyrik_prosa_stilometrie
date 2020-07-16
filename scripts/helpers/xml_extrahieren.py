import xml.etree.ElementTree as ET
import os

dateien = ['DEU026','DEU034','DEU035','DEU036','DEU044','DEU046','DEU051','DEU053','DEU056','DEU059','DEU060','DEU064',
           'DEU066','DEU070','DEU071','DEU075','DEU088','DEU089','DEU092']

document = '/home/teresa/Uni/Master/Semester 3/stilometrie/lyrik_prosa_stilometrie/corpus/ELTeC-deu-master/level0/DEU026.xml'

outpath = '../corpus/autoren_epik/'

# finde pro Szene vorkommende Personen und speichere diese als Liste in einer Liste

for datei in dateien:
    root = ET.parse('../corpus/ELTeC-deu-master/level0/' + datei + '.xml').getroot()
    NS = {'tei': 'http://www.tei-c.org/ns/1.0'}

    text = ''
    for div_tag in root.findall(".//tei:p", namespaces=NS):
        if type(div_tag.text) == str:
            text+= div_tag.text
            text+=' '

    if os.path.exists(outpath + str(datei) + ".txt"):
        txtFile = open(outpath + str(datei) + ".txt", "w")
        txtFile.write('')
        txtFile.close()
    txtFile = open(outpath + str(datei) + ".txt", "a")
    for word in datei:
        txtFile.write(text)
    txtFile.close()
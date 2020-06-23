import csv
import os
from collections import Counter

def mfw(path):
    ''' zählt Wordhäufigkeiten pro Segment '''
    stopword = open("de_stopwords.txt")
    stopwords = stopword.read()
    words = []
    for text in os.listdir(path):
        t = open(path + '/' + text, 'r')
        f = t.read()
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


### erkennt direkte Rede in den Dokumenten und rechnet die relative Häufigkeit 'aus'
def count_merkmale(Partition, merkmal):
    ''' zählt nur, ob irgendeines der Merkmale in merkmal in Segment vorkommt ungeachtet der Häufigkeit'''
    häufigkeitSegment = 0
    anzahl = 0
    for text in os.listdir(Partition):
        startIndex = 0
        t = open(Partition + "/" + text, "r")
        f = t.read()
        if text.endswith(".txt"):
            anzahl += 1
            for e in merkmal:
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

def zeta_per_word(Partition, merkmal):
    ''' zählt für jedes Merkmal in merkmal, ob es im Segment vorkommt '''
    häufigkeitSegment = 0
    anzahl = 0
    dic = {}
    for wort in merkmal:
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

def save_zeta(pfadV, pfadZ, merkmal, filename):
    lyrik = zeta_per_word(pfadZ, merkmal)
    prosa = zeta_per_word(pfadV, merkmal)
    zetas = {}
    for wort in merkmal:
        zetas[wort] = zeta(lyrik[wort], prosa[wort])

    w = csv.writer(open(filename+".csv", "w"))
    for key, val in zetas.items():
        w.writerow([key, val])
    return zetas

# ### Ziel

mfw = mfw('../corpus/corpora_gesamt/')
ohne_dupl = drop_duplicates(mfw)
nur_dupl = mfw_only_duplicates(mfw)
emotion = ['liebreich','angst', 'ängstlich', 'trauer', 'traurig', 'zornig', 'zorn', 'verachtungsvoll', 'verachtung',
           'schuld', 'schuldig', 'liebe',  'geliebt', 'liebevoll', 'stolz', 'scham', 'schämen', 'überrasschung',
           'überrascht', 'sorge', 'sorgenvoll', 'ekel', 'ekeln', 'angeekelt', 'neid', 'neidisch', 'neidvoll',
           'glücklich', 'glück', 'freude', 'freudig', 'freuen', 'erleichterung', 'erleichtert', 'vergnügt', 'vergnügen',
           'zufrieden', 'zufriedenheit', 'verzweiflung', 'verzweifelt', 'verlegenheit', 'verlegen', 'aufregung',
           'aufgeregt', 'aufregen', 'spannung', 'gespannt', 'erregung', 'erregt', 'hoffen', 'hoffnung', 'befriedigt',
           'langweilig', 'langeweile', 'mitgefühl', 'mitfühlen', 'enttäuscht', 'enttäuschung', 'frust', 'frustriert',
           'eifersucht', 'eifersüchtig', 'wut', 'wütend', 'reue', 'schock', 'schockiert', 'zuneigung', 'verärgert',
           'verärgerung', 'erwartungsvoll', 'erwartung', 'vorfreude', 'scheu', 'gelassen', 'gelassenheit', 'mut',
           'mutig', 'neugierde', 'neugierig', 'depression', 'depressiv', 'niedergeschlagenheit', 'niedergeschlagen',
           'lustvoll', 'lust', 'rausch', 'einfühlend', 'einfühlsam', 'euphorisch', 'euphorie', 'dankbarkeit', 'dankbar',
           'hass', 'entsetzt', 'entsetzen', 'demütigung', 'demütig', 'demut', 'interesse', 'interessiert', 'einsamkeit',
           'einsam', 'empörung', 'empört', 'vertrauen', 'qualvoll', 'qual', 'gleichgültigkeit', 'gleichgültig',
           'fröhlichkeit', 'fröhlich', 'schadenfroh', 'schadenfreude', 'schmerz', 'melancholie', 'melancholisch',
           'panik', 'panisch']
nomen = ['freude','vertrauen', 'angst','überraschung', 'trauer', 'ekel', 'wut', 'mitgefühl', 'liebe']
anf = ['\"', '»', '«']
instanz_epik = ['er', 'sie']
instanz_lyrik = ['ich']
sprechmarker = ['sagen', 'sprechen', 'fragen', 'antworten', 'schreien', 'jammern']
sprechmarker_lang = ['abfertigen', 'abhören','ablehnen','abraten','abschlagen','abschweifen','absprechen','abstreiten',
                     'andeuten','anerkennen', 'anfechten','angeben','angreifen','ankünden','anraten','anschneiden',
                     'antworten','anvertrauen','anweisen','artikulieren','aufmuntern','aufschneiden','auftischen',
                     'aufzeigen','ausdrücken','Ausflüchte machen','ausforschen','ausfragen','ausführen','aushorchen',
                     'ausplaudern','ausquetschen','aussagen', 'äußern', 'sich aussprechen','austrommeln','ausweichen',
                     'bedanken', 'bedeuten', 'befehlen','befragen','befürchten','begründen','beharren auf','behaupten',
                     'beichten','bejahen', 'bekennen', 'beklagen', 'bekräftigen', 'bekunden', 'beleuchten', 'bemänteln',
                     'bemerken', 'berichten', 'berichtigen', 'beruhigen', 'besagen', 'Bescheid geben', 'beschönigen',
                     'beschreiben','beschwören','bestätigen','bestehen auf','bestimmen','bestreiten','beten','beteuern',
                     'betonen','betteln','beweisen','bezeichnen','bezeugen','bitten','brabbeln','bramarbasieren',
                     'breittreten','brüllen','brummen','dabei bleiben','daherreden','darlegen','dartun','definieren',
                     'dementieren','demonstrieren', 'den Mund vollnehmen','deuteln','dick auftragen','dazwischenfahren',
                     'drohen', 'ein Ohr abkauen','einräumen','einreden','einschärfen','einwenden','einwilligen','empfehlen',
                     'entgegenhalten','entgegnen','enthüllen','entkräften','entschuldigen','erdichten','erfinden',
                     'ergänzen','erinnern','erklären','erkundigen', 'ermahnen','ermuntern','ermutigen','erörtern','erschließen',
                     'erwähnen','erweisen', 'erwidern','erzählen','evident machen','fabulieren','faseln','feststellen',
                     'flehen','flunkern','flüstern','folgern','fordern','fragen', 'geheim halten','geltend machen',
                     'gestehen','glauben','herausposaunen','herausreden', 'herausschreien','herumkritteln','hervorheben',
                     'hindeuten','hinweisen','hinzufügen','höhnen','in Abrede stellen','in Frage stellen','ins Gesicht sagen',
                     'jammern','keuchen','klagen','klatschen','klöhnen','konstatieren','krächzen','kritisieren','kundgeben',
                     'kundtun','labern','lächeln','lachen','lallen','leugnen','lispeln','loben','mahnen','meinen','mitteilen',
                     'munkeln','murmeln','nachfragen','nachweisen','näseln','negieren','nennen','nicht wahr haben wollen',
                     'nuscheln','offenbaren','palavern','petzen','plaudern','plauschen','prahlen','quasseln','quatschen',
                     'raten','ratschen','raunen','Rede und Antwort stehen','reden wie ein Buch','reden wie ein Wasserfall',
                     'reinen Wein einschenken','röcheln','rufen','sabbeln','salbadern','schildern','schleimen','schließen',
                     'schluchzen','schmeicheln','schnacken','schnarren','schnattern','schreien','schwadronieren','schwatzen',
                     'schwätzen','schwören','seiern','sich verhaspeln','skizzieren','sondieren','sprechen','stammeln',
                     'stottern','tadeln','tratschen','trösten','tuscheln','überinterpretieren','überreden','übertreiben',
                     'überzeugen','umreißen','umschreiben','unken','Unsinn verzapfen','unterhalten','unterstreichen',
                     'unterstützen','veranschaulichen','verbürgen','verdrehen','verfälschen','verhören','verklickern',
                     'verkünden','verlangen','verlautbaren','verleugnen','vernehmen','verneinen','verraten','verschleiern',
                     'versichern','versprechen','vertiefen','verwerfen','verzerren','vorbringen','vorenthalten','vorgeben','warnen',
                     'weit ausholen','widerlegen','widerrufen','widersprechen','wiederholen','wissen wollen','zeigen',
                     'zitieren','zu bedenken geben','zugeben','zugestehen','zum Besten geben','zureden','zurücknehmen',
                     'zurufen','zustimmen']
# POS = ['JJ', 'VBZ', 'NN']


# merkmal = {'emotion': emotion, 'nomen': nomen, 'anf': anf, 'instanz_epik': instanz_epik, 'instanz_lyrik': instanz_lyrik,
#            'sprechmarker': sprechmarker, 'sprechmarker_lang':sprechmarker_lang, 'ohne_dupl': ohne_dupl, 'nur_dupl': nur_dupl}
merkmal = {'sprechmarker_lang':sprechmarker_lang}
segmentcount = ['100', '500', '1000']
for k,v in merkmal.items():
    for c in segmentcount:
        pfadZ = '../corpus/segmente/segmentelyrik_' + c
        pfadV = '../corpus/segmente/segmenteepik_' + c

        save_zeta(pfadV, pfadZ, v, '../results/zeta/' + k + '_' + c)


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




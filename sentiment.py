import json, re

with open('word_list.json') as afinnJson:
    afinn = json.load(afinnJson)


def negativity (phrase):
    
    noPunctuation = re.sub('[^a-zA-Z ]+', ' ', phrase)
    noPunctuation = re.sub(' {2,}', ' ', phrase)
    tokens = noPunctuation.lower().split(' ')
    hits   = 0
    words  = []

    def addPush(t, score):
        nonlocal hits
        hits -= score
        words.append(t)

    for t in tokens:
        if t in afinn and afinn[t] < 0:
            addPush(t, afinn[t])


    return {
        'score'       : hits,
        'comparative' : hits / len(tokens),
        'words'       : words
    }



def positivity(phrase):

    noPunctuation = re.sub('[^a-zA-Z ]+', ' ', phrase)
    noPunctuation = re.sub(' {2,}', ' ', phrase)
    tokens = noPunctuation.lower().split(" ")
    hits   = 0
    words  = []

    def addPush(t, score):
        nonlocal hits
        hits += score
        words.append(t)

    for t in tokens:
        if t in afinn and afinn[t] > 0:
            addPush(t, afinn[t])

    return {
        'score'       : hits,
        'comparative' : hits / len(tokens),
        'words'       : words
    }


def analyze(phrase):

    pos = positivity(phrase)
    neg = negativity(phrase)

    return {
        'score'       : pos['score'] - neg['score'],
        'comparative' : pos['comparative'] - neg['comparative'],
        'positive'    : pos,
        'negative'    : neg
    }


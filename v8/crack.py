
from math import log10
import cipher

PATH = 'v6\english_quadgrams.txt'

class ngram_score(object):
    def __init__(self, ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in open(ngramfile).readlines():
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        #calculate log probabilities
        for key in list(self.ngrams.keys()):
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       
def crack(text):
    score = ngram_score(PATH)

    allCeaser = {}
    allRailfence = {}

    def _test(d):
        # _max = max(d, key = d.get)
        # _max = {_max:d[_max]}
        # return _max
        # _max = max(d, key=lambda x:x['price'])
        # _min = min(d, key=lambda x:x['price'])

        # return _max, _min
        
        highest_score = float('-inf')
        highest_key = None

        for key, value in d.items():
            score = value.get('score', 0)
            if score > highest_score:
                highest_score = score
                highest_key = key

        if highest_key is not None:
            return [highest_key, d[highest_key]]
        else:
            return None


    def _crackCeaser(text):
        for i in range(1, 27):
            de = cipher.decipher(text, i, "Ceaser")
            if de:
                allCeaser[de] = {'score':score.score(de), 'key':i}

        # print('Most Probable Ceaser:', _test(allCeaser))

    def _crackRailfence(text, maxKey=100):
        for i in range(1, maxKey + 1):
            de = cipher.decipher(text, i, "Railfence")
            if de:
                allRailfence[de] = {'score':score.score(de), 'key':i}

        # print('Most Probable Railfence:', _test(allRailfence))

    _crackCeaser(text)
    yield [allCeaser, _test(allCeaser)]

    _crackRailfence(text)
    yield [allRailfence, _test(allRailfence)]

# {'help':{'score':-65, 'key':8}, 'me':{'score':138, 'key':128}, 'please':{'score':-6500, 'key':9187345}}

from math import log10
import cipher

PATH = 'english_quadgrams.txt'

class ngram_score:
    def __init__(self, ngramfile, sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        with open(ngramfile) as f:
            for line in f.readlines():
                key, count = line.split(sep) 
                self.ngrams[key] = int(count)

        self.times = []
        self.avrgTime()
        
        import re
        import time
        self.time = time

        self.regex = re.compile('[^a-zA-Z]')
        #First parameter is the replacement, second parameter is your input string

    def avrgTime(self):
        try:
            self.averageTime = sum(self.times) / len(self.times)
        except ZeroDivisionError:
            self.averageTime = 0

    def score(self, text):
        ''' compute the score of text '''
        text = self.regex.sub('', text.lower())
        text = [text]

        t1 = self.time.time()

        score = 0
        for ngram, freq in self.ngrams.items():
            # too slow (~0.1-0.2s)
            score += text.count(ngram) * freq

        self.times.append(self.time.time() - t1)
        self.avrgTime()

        return score
       
def crack(text):
    score = ngram_score(PATH)

    allCeaser = {}
    allRailfence = {}
    allAffine = {}

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
            de = cipher.decipher(text, i, None, "Ceaser")
            if de:
                allCeaser[de] = {'score':score.score(de), 'deciphered':de, 'key':i}

        # print('Most Probable Ceaser:', _test(allCeaser))

    def _crackRailfence(text, maxKey=100):
        for i in range(1, maxKey + 1):
            de = cipher.decipher(text, i, None, "Railfence")
            if de:
                allRailfence[de] = {'score':score.score(de), 'deciphered':de, 'key':i}

    def _crackAffine(text, maxKey=100):
        for a in range(1, maxKey + 1):
            for b in range(1, maxKey + 1):
                try:
                    de = cipher.decipher(text, a, b, "Affine")
                except ValueError:
                    pass
                if de:
                    allAffine[de] = {'score':score.score(de), 'deciphered':de, 'key':a, 'key2':b}

        # print('Most Probable Affine:', _test(allAffine))

    _crackCeaser(text)
    yield [allCeaser, _test(allCeaser)]
    print(f'Average time: {score.averageTime}, time total: {score.averageTime*26}, next predicted time: {score.averageTime*100}')

    _crackRailfence(text)
    yield [allRailfence, _test(allRailfence)]
    print(f'Average time: {score.averageTime}, time total: {score.averageTime*100}, next predicted time: {score.averageTime*100*100}')

    _crackAffine(text)
    yield [allAffine, _test(allAffine)]
    print(f'Average time: {score.averageTime}, time total: {score.averageTime*100*100}, next predicted time: ')

# {'help':{'score':-65, 'key':8}, 'me':{'score':138, 'key':128}, 'please':{'score':-6500, 'key':9187345}}
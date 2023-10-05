
from math import log10
from crackWindow import CrackProgress
import tkinter as tk
import threading
import cipher
import time

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
       
def crack(text, rootWindow=None, mainloop=True):
    global progressCeaser, progressRailfence, progressTotal, allCeaser, allRailfence, widget

    if not rootWindow:
        rootWindow = tk.Tk()

    score = ngram_score(PATH)

    progressTotal = 0
    progressCeaser = 0
    progressRailfence = 0

    allCeaser = {}
    allRailfence = {}

    def _test(d):
        _max = max(d, key = d.get)
        _max = {_max:d[_max]}
        return _max

    def _crackCeaser(text):
        global progressCeaser, progressRailfence, progressTotal, allCeaser, allRailfence
        for i in range(1, 27):
            de = cipher.decipher(text, i, "Ceaser")
            if de:
                allCeaser[de] = score.score(de)

            time.sleep(0.2)

            progressCeaser = i / 26 * 100
            progressTotal = (progressRailfence + progressCeaser) / 2
            rootWindow.after(50, _ProgressBarUpdate())

        # print('Most Probable Ceaser:', _test(allCeaser))

    def _crackRailfence(text, maxKey=100):
        global progressCeaser, progressRailfence, progressTotal, allCeaser, allRailfence
        for i in range(1, maxKey + 1):
            de = cipher.decipher(text, i, "Railfence")
            if de:
                allRailfence[de] = score.score(de)

            time.sleep(0.1)

            progressRailfence = i / maxKey * 100
            progressTotal = (progressRailfence + progressCeaser) / 2
            rootWindow.after(50, _ProgressBarUpdate())

        # print('Most Probable Railfence:', _test(allRailfence))

    def _ProgressBarUpdate():
        global progressCeaser, progressRailfence, progressTotal, widget
        # widget.TotalBar.config(value=progressTotal)
        # widget.CeaserBar.config(value=progressCeaser)
        # widget.RailfenceBar.config(value=progressRailfence)

        # widget.TotalBar.set(progressTotal)
        # widget.CeaserBar.set(progressCeaser)
        # widget.RailfenceBar.set(progressRailfence)
        
        # widget.TotalBarValue.set(progressTotal)
        # widget.CeaserBarValue.set(progressCeaser)
        # widget.RailfenceBarValue.set(progressRailfence)

        widget.TotalBar['value'] = progressTotal
        widget.CeaserBar['value'] = progressCeaser
        widget.RailfenceBar['value'] = progressRailfence

        # print(progressTotal)
        # print(progressCeaser)
        # print(progressRailfence)

        rootWindow.update()
    
    def ProgressBarUpdate():
        try:
            while True:
                _ProgressBarUpdate()
                time.sleep(0.05)
        except:
            pass

    widget = CrackProgress(rootWindow)
    
    # ceaserThread = threading.Thread(target=_crackCeaser, args=[text])
    # railfenceThread = threading.Thread(target=_crackRailfence, args=[text])
    # progressBarThread = threading.Thread(target=ProgressBarUpdate)
    
    # ceaserThread.start()
    # railfenceThread.start()
    # progressBarThread.start()

    widget.pack(expand=True, fill="both")
    # rootWindow.update()

    rootWindow.after(50, _crackCeaser(text))
    rootWindow.after(50, _crackRailfence(text))

    if mainloop:
        rootWindow.mainloop()

    return [allCeaser, _test(allCeaser)], [allRailfence, _test(allRailfence)]

from math import log10
from crackWindow import CrackProgress
import tkinter as tk
import threading
import cipher
import time

PATH = 'v4\english_quadgrams.txt'

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
       
def crack(text, rootWindow=tk.Tk(), mainloop=True):
    global progressCeaser, progressRailfence, progressTotal, allCeaser, allRailfence, widget
    score = ngram_score(PATH)

    progressTotal = 0
    progressCeaser = 0
    progressRailfence = 0

    allCeaser = {}
    allRailfence = {}

    def _crackCeaser(text):
        global progressCeaser, progressRailfence, progressTotal, allCeaser, allRailfence
        for i in range(1, 27):
            de = cipher.decipher(text, i, "Ceaser")
            if de:
                allCeaser[de] = score.score(de)

            time.sleep(0.2)

            progressCeaser = i / 26 * 100
            progressTotal = (progressRailfence + progressCeaser) / 2

    def _crackRailfence(text, maxKey=100):
        global progressCeaser, progressRailfence, progressTotal, allCeaser, allRailfence
        for i in range(1, maxKey + 1):
            de = cipher.decipher(text, i, "Railfence")
            if de:
                allRailfence[de] = score.score(de)

            time.sleep(0.1)

            progressRailfence = i / maxKey * 100
            progressTotal = (progressRailfence + progressCeaser) / 2
    
    def ProgressBarUpdate():
        try:
            global progressCeaser, progressRailfence, progressTotal, widget
            while True:
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
                time.sleep(0.05)
        except:
            pass

    widget = CrackProgress(rootWindow)
    
    ceaserThread = threading.Thread(target=_crackCeaser, args=[text])
    railfenceThread = threading.Thread(target=_crackRailfence, args=[text])
    progressBarThread = threading.Thread(target=ProgressBarUpdate)
    
    ceaserThread.start()
    railfenceThread.start()
    progressBarThread.start()

    widget.pack(expand=True, fill="both")
    if mainloop:
        rootWindow.mainloop()

    print(allCeaser)
    print(allRailfence)
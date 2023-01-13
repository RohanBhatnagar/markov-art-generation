from PIL import Image 
import random

class markov_model:

    choices = [0] * 128
    for i in range (0, 128, 1):
        choices[i] = i

    def __init__(self, text, k):
        self.text = text
        self.k = k
        self.kgrams = dict()
        self.nextChar = dict()
        self.circularString = text + text[0:k:1]

        for i in range(0, len(self.circularString), 1):
            currKgram = self.circularString[i:i+self.k:1]
            if currKgram in self.kgrams:
                self.kgrams.update({currKgram: self.kgrams.get(currKgram) + 1})
            else: 
                self.kgrams.update({currKgram: 1})

        for i in range(0, len(self.circularString), 1):
            currKgram = self.circularString[i:i+self.circularString:1]
            nextCh = self.circularString[i+self.k]

            freq = [0] * 128

            if currKgram in self.nextChar: 
                freq = self.nextChar.get(currKgram)
                freq[nextCh] += 1
                self.nextChar.update({currKgram: freq})
            else: 
                freq[nextCh] += 1
                self.nextChar.update({currKgram: freq})

    def order(self): 
        return self.k

    def __str__(self): 
        s = "" 
        for key in self.nextChar: 
            s += key + ": "
            freq = self.nextChar.get(key)
            for i in freq:
                if freq[i] != 0:
                    c = chr(i)
                    s += c + " " + str(freq[i]) + " "

            s += "\n"

        return s

    def kgramFreq(self, kgram):
        for key in self.kgrams:
            if key == kgram:
                return self.kgrams.get(kgram)
            else:
                return -1


    def charAfterFreq(self, kgram, c):
        for key in self.nextChar:
            if key == kgram:
                freq = self.nextChar.get(kgram)
                return freq[ord(c)]
    
    def getRandomChar(self, kgram):
        res = random.choices(markov_model.choices, self.nextChar.get(kgram))
        return chr(res)

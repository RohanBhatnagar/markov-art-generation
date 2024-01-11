from PIL import Image 
import random

class markov_model:


    def __init__(self, text, k):
        self.text = text
        self.k = k
        self.kgrams = dict()
        self.nextChar = dict()
        self.circularString = text
        self.unique_colors = 0

        # dict - contains unique kgrams and frequencies. 
        for i in range(0, len(text) - k, 6):
            currKgram = self.circularString[i:i+k]
            if currKgram in self.kgrams:
                self.kgrams.update({currKgram: self.kgrams.get(currKgram) + 1})
            else: 
                self.kgrams.update({currKgram: 1})

        for i in range(0, len(self.circularString) - k - 6, 6):
            currKgram = self.circularString[i:i+k:1]
            nextColor = self.circularString[i+k: i+k+6]

            freq = dict()

            if currKgram in self.nextChar: 
                freq = self.nextChar.get(currKgram)
            
            if nextColor not in freq: 
                self.unique_colors += 1
                freq[nextColor] = 1
            else:
                freq[nextColor] += 1
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
                return freq[c]
    
    def getRandomChar(self, kgram):
        dictionary = self.nextChar.get(kgram)
        population = list(dictionary.keys())
        weights = list(dictionary.values())
        next_color = random.choices(population, weights)
        return next_color[0]

# -*- coding: UTF-8 -*-
# Author johan Öh
# class used to distribute a set of characters randomly according to the
# distribution info provided by the class distribution

import random

class Distributor:
    
    def __init__(self,dist):
        self.totalcount = 0
        self.currchar = ""
        self.dist = dist
    
    # used to pick a char at random from the sorted tuple according
    # to the distribution value 0.0 - 1.0
    def _nonUniformCharPick(self,sortedTuple):
        ran = random.uniform(0.0,1.0)
        i = 0.0
        for x in sortedTuple:
            i += x[1]
            if ran < i:
                self.currchar = x[0]
                return self.currchar
            
    # Returns a randomly generated char according to the distribution
    # and remembers the last generated this is the input for the next char to be
    # generated
    def getRandChar(self):
        dist = self.dist
        if  not self.currchar:
            # create a tuple sorted by the value of occurence from dict
            sortedTuple = sorted(dist.charDistTotal.items(), key=lambda x:x[1])
            return self._nonUniformCharPick(sortedTuple)
        elif self.currchar in dist.distNext:
            chardict = dist.distNext[self.currchar]
            sortedTuple = sorted(chardict.items(), key=lambda x:x[1])
            return self._nonUniformCharPick(sortedTuple)
        else:
            self.currchar =""
            return self.getRandChar()  
        
    # Returns a string of length "length" with randomly distributed chars
    def getRandString(self,length): 
        tmpStr=""
        for p in range(0,length):
            tmpStr += self.getRandChar()
        return tmpStr

# -*- coding: UTF-8 -*-
# Author johan Öh
# class Distribution works as a container for letter distributions in a text
# dictionary map char -> distribution 
# and a twodimensional dictionary that maps each char to a dictionary of second 
# chars and their distribution answering the question if char is an "a" 
# what is the next char and how common is it ie {"a":{ "b" :3.0, "c":4.0,...}}

class Distribution:
    
    def __init__(self):
        
        self.charsTotal = 0 # count all added chars
        self.distNext = {} # keep count of the "current char" and "next char" and how common it is
        self.totalForChars = {} # Total of chars that follows specific char
        self.charDistTotal = {} #Keep count of the total distribution of characters
       
        
    # Adds a char to be counted
    def addChar(self,curchar,nextchar):
        #increment the total char counter
        self.charsTotal+=1.0
        # check if char already i dict
        if curchar in self.distNext:
            self.totalForChars[curchar] += 1.0
            self.charDistTotal[curchar] += 1.0
            # check if the next char exists in dict if so 
            # increment the occurence else add
            if nextchar in self.distNext[curchar]:
                self.distNext[curchar][nextchar] += 1.0
            else:
                self.distNext[curchar][nextchar] = 1.0
        else:
            self.distNext[curchar] = {nextchar:1.0}
            self.totalForChars[curchar] = 1.0
            self.charDistTotal[curchar] = 1.0
            
    def addSingleChar(self, singleChar):
        self.charsTotal+=1.0
        if singleChar in self.distNext:
            self.totalForChars[singleChar] += 1.0
            self.charDistTotal[singleChar] += 1.0
        else:
            self.totalForChars[singleChar] = 1.0
            self.charDistTotal[singleChar] = 1.0
            
    def displayDist(self):
        for x in self.distNext:
            print("Total in "+x+" = "+str(self.totalForChars[x]))
            for y in self.distNext[x]:
                print(str(y)+" : "+str(self.distNext[x][y]))
                
    # calculates the distribution from the added and counted characters in the
    # distribution object.
    @staticmethod   
    def calculateDistribution(distribution):
        for x in distribution.distNext:
            for y in distribution.distNext[x]:
                distribution.distNext[x][y] = distribution.distNext[x][y]/distribution.totalForChars[x]
        for l in distribution.charDistTotal:
             distribution.charDistTotal[l] = distribution.charDistTotal[l]/distribution.charsTotal
    
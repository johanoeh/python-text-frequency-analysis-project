# -*- coding: UTF-8 -*-
# Author johan Öh
#
import sys, getopt,codecs 
from stats import Distribution
from generator import Distributor
from distributionhandler import DistributionHandler
from ngramcalculator import NGramCalculator

class FileWriter:
    def __init__(self,pathToFile):
        self.pathToFile=pathToFile
        self.file =codecs.open(pathToFile,'w','utf-8')
    def write(self, strToWrite):
        self.file.write(strToWrite)
    def close(self):
        self.file.close()

class FileReader:
    def __init__(self,pathToFile):
        self.pathToFile=pathToFile
    def open():
        self.file = codecs.open(self.pathToFile,'r','utf-8')
        return self.file
    def close(self):
        self.file.close()
        
def readfile(path):
    f = codecs.open(path,'r','utf-8')
    rows=[]
    for l in f:
        l = "".join(l.lower())
        rows.append(l)
    return rows
    f.close()
    
def writeStatsToFile(resource,grams):
    print(resource)
    f = codecs.open(resource,'w','utf-8')
    i=0
    limit = 10
    for l in grams:
       f.write(l[0]+" : " + str(l[1])+"\n")
       print(l[0]+" : " + str(l[1]))
       if i > limit:
           break
       i+=1
    f.close()
    
def generate(inputFile, outputFile, nLines):
    dist = Distribution()
    DistributionHandler.calcDistribution(readfile(inputFile),dist)
    printDistributedString(dist,nLines)
    writeRandomText(outputFile,dist,nLines)


def writeRandomText(outputFile,dist,nLines):
    distrb = Distributor(dist)
    writer = FileWriter(outputFile+".generated");
    for i in range(0,nLines):
        writer.write(distrb.getRandString(100)+"\n")
    writer.close()
    
def printDistributedString(dist,nLines): 
    distrb = Distributor(dist)
    for p in range(1,nLines):
        print(distrb.getRandString(100))
        
def printgrams(resource,grams,limit):
    print(resource)
    i=0
    for l in grams:
       print(l[0]+" : " + str(l[1]))
       if i > limit:
           break
       i+=1
   
def textAnalyzeALL(infile,outfile,n):
    if not n:
        n = 4
    rows = readfile(infile)
    for i in range(1,n):
        analyzeText(infile, outfile,i, rows)

def analyzeText(infile,outfile,nGramType,rows):
    
    if not rows:
        rows = readfile(infile)
    
    gramName =""
    nGram = {}
    
    if nGramType == 1:
        gramName = "Monograms"
    elif nGramType == 2:
        gramName = "Digrams"
    elif nGramType == 3:
        gramName ="Trigrams"
    elif nGramType == 4:
        gramName = "Tetragram"
    elif ngGramType == 5:
        gramName = "Pentagram"
    else:
        gramName = str(nGramType)+":gram"
        
    
    nGrams = {nGramType:nGram}
    NGramCalculator.countGrams(rows, nGrams)
    gramSorted = sorted(nGram.items(), key=lambda x:x[1], reverse = True)
    #printgrams(gramName, gramSorted, 10)
    writeStatsToFile(outfile+"."+gramName.lower(), gramSorted)


def main(argv):
    
   inputfile = ''
   outputfile = ''
   ngram = ""
   nLines = 0
   
   a = False
   m = False
   d = False
   t = False
   g = False
   n = False
   
   try:
      opts, args = getopt.getopt(argv,"hi:o:n:madtg:r:",["ifile=","ofile=","ngram","monogram","digram","trigram","all","generate","rows"])
   except getopt.GetoptError:
      print ('freek.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
      
   for opt, arg in opts:
      if opt == '-h':
         print('freek.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-m", "--monogram"):
         m = True
      elif opt in ("-a", "--all"):
         a = True
      elif opt in ("-d", "--digram"):
         d = True
      elif opt in ("-t", "--trigram"):
         t = True
      elif opt in ("-g", "--generate"):
         g = True
         nLines = int(arg)
      elif opt in ("-n", "--ngrams"):
         ngram = int(arg)
         n = True
         
   if not inputfile or not outputfile:
       print("Error")
   elif a:
       textAnalyzeALL(inputfile,outputfile,4)
   elif m :
       lines=""
       analyzeText(inputfile, outputfile,1,lines)
   elif d :
        lines=""
        analyzeText(inputfile, outputfile,2,lines)
   elif t:
       lines=""
       analyzeText(inputfile, outputfile,3,lines)
   elif t:
       lines=""
       analyzeText(inputfile, outputfile,3,lines)
   elif n:
       if not ngram:
           print("-n --ngram flag requires integer argument")
           sys.exit(2)
       else:
           textAnalyzeALL(inputfile,outputfile,ngram+1)
   elif g:
      DistributionHandler.generate(inputfile, outputfile, nLines)
 
if __name__ == "__main__":
   main(sys.argv[1:])


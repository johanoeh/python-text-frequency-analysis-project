# -*- coding: UTF-8 -*-
# Author johan Öh
#
import sys, getopt

from distributionhandler import DistributionHandler
from ngramcalculatorhandler import NgramCalculationHandler


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
      print ('freak.py -i <inputfile> -o <outputfile>')
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
       NgramCalculationHandler.textAnalyzeALL(inputfile,outputfile,4)
   elif m :
       lines=""
       NgramCalculationHandler.analyzeText(inputfile, outputfile,1,lines)
   elif d :
        lines=""
        NgramCalculationHandler.analyzeText(inputfile, outputfile,2,lines)
   elif t:
       lines=""
       NgramCalculationHandler.analyzeText(inputfile, outputfile,3,lines)
   elif t:
       lines=""
       NgramCalculationHandler.analyzeText(inputfile, outputfile,3,lines)
   elif n:
       if not ngram:
           print("-n --ngram flag requires integer argument")
           sys.exit(2)
       else:
           NgramCalculationHandler.textAnalyzeALL(inputfile,outputfile,ngram+1)
   elif g:
      DistributionHandler.generate(inputfile, outputfile, nLines)
 
if __name__ == "__main__":
   main(sys.argv[1:])


from dataaccess import DAO
from ngramcalculator import NGramCalculator
class NgramCalculationHandler:
    
    @staticmethod
    def textAnalyzeALL(infile,outfile,n):
        dao =DAO()
        if not n:
            n = 4
        rows = dao.getTextRows(infile)
        for i in range(1,n):
            NgramCalculationHandler.analyzeText(infile, outfile,i, rows)
            
    @staticmethod
    def analyzeText(infile,outfile,nGramType,rows):
        dao = DAO()
        if not rows:
            rows = dao.getTextRows(infile)

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
        dao.saveNGramDistribution(outfile+"."+gramName.lower(),gramSorted)
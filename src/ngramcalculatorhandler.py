class NgramCalculationHandler:
    
    @staticmethod
    def textAnalyzeALL(infile,outfile,n):
        if not n:
            n = 4
        rows = readfile(infile)
        for i in range(1,n):
            analyzeText(infile, outfile,i, rows)
            
    @staticmethod
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
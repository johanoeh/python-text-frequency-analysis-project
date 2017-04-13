class NGramCalculator:
    
    @staticmethod    
    def countNGrams(s,gap,nGramFrequency):
        counter = 0
        for i in range(0,len(s)-gap):
            substr = s[i:i+gap]
            # check that the sequence consists of only alphabethical characters [a-ö]
            if substr.isalpha():
                counter +=1
                if substr in nGramFrequency:
                  tempCount = nGramFrequency[substr]
                  nGramFrequency[substr] = tempCount + 1.0
                else:
                    nGramFrequency[substr] = 1.0
        return counter
    
    @staticmethod           
    def countGrams(rows,nGrams):
        tstr=""
        for s in rows:
            tstr+=s    
        for gram in nGrams :
            noNgrams = NGramCalculator.countNGrams(tstr,gram,nGrams[gram])
            NGramCalculator.calcNGramDistribution(nGrams[gram],noNgrams)
            #NGramCalculator.checkDistribution(nGrams[gram])
    
    @staticmethod
    def checkDistribution(nGram):
        count =0.0
        for entry in nGram:
            count+= nGram[entry]
        print(count)
            
         
    @staticmethod
    def calcNGramDistribution(nGram,divisor):
        for gram in nGram:
            nGram[gram] = (nGram[gram]/divisor)*100
        
                
class NGramStatsHandler:
    def __init__(self):
         self.nGramFrequency = {}
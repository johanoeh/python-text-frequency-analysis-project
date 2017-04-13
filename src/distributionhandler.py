import codecs 
from stats import Distribution
from generator import Distributor
from filewriter import FileWriter
class DistributionHandler:
    
    @staticmethod
    def calcDistribution(stringList,dist):
        tmpStr=""
        for s in stringList:
            tmpStr +="".join(s)
        for x in range(0,len(tmpStr)-1):
                dist.addChar(tmpStr[x],tmpStr[x+1])
        dist.calculateDistribution(dist)

    @staticmethod
    def readfile(path):
        f = codecs.open(path,'r','utf-8')
        rows=[]
        for l in f:
            l = "".join(l.lower())
            l = "".join(l.split())
            rows.append(l)
        f.close()
        return rows
        
        
    @staticmethod   
    def writeRandomText(outputFile,dist,nLines):
        distrb = Distributor(dist)
        writer = FileWriter(outputFile+".generated");
        for i in range(0,nLines):
            writer.write(distrb.getRandString(100)+"\n")
        writer.close()
    
    @staticmethod
    def generate(inputFile, outputFile, nLines):
        dist = Distribution()
        DistributionHandler.calcDistribution(DistributionHandler.readfile(inputFile),dist)
        #printDistributedString(dist,nLines)
        DistributionHandler.writeRandomText(outputFile,dist,nLines)
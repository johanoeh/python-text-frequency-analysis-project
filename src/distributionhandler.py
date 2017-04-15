import codecs 
from stats import Distribution
from generator import Distributor
from dataaccess import DAO
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
    def generate(inputFile, outputFile, nLines):
        dao = DAO()
        dist = Distribution()
        DistributionHandler.calcDistribution(dao.getStrippedTextRows(inputFile),dist)  
        distrb = Distributor(dist)
        lines = []
        for i in range(0,nLines):
            lines.append(distrb.getRandString(100))
        dao.saveText(lines,outputFile)
        
    @staticmethod
    def printDistributedString(dist,nLines): 
        distrb = Distributor(dist)
        for p in range(1,nLines):
            print(distrb.getRandString(100))
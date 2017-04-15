from filereader import FileReader
from filewriter import FileWriter

class Parser:
    def __init__(self,fileObject):
        self.fileObject = fileObject       
    def parse(self):
        rows =[]
        for l in self.fileObject:
            l = "".join(l.lower())
            rows.append(l)
        return rows
    
class DistParser:
     def __init__(self,fileObject):
        self.fileObject = fileObject       
     def parse(self):
        rows =[]
        for l in self.fileObject:
            l = "".join(l.lower())
            l = "".join(l.split())
            rows.append(l)
        return rows

class DAO :
    def __init__(self):
        print("initializing")
        
    def getTextRows(self, resource):
        fileReader = FileReader(resource)
        parser = Parser(fileReader.open())
        return parser.parse()
    
    def getStrippedTextRows(self, resource):
        fileReader = FileReader(resource)
        parser = DistParser(fileReader.open())
        return parser.parse()
    
    def saveText(self,textRows,resource):
        fileWriter = FileWriter(resource)
        for l in textRows:
            fileWriter.write(l+"\n")
        fileWriter.close()
        
    def saveNGramDistribution(self,resource, nGramDistribution):
        fileWriter = FileWriter(resource)
        for l in nGramDistribution:
           fileWriter.write(l[0]+"," + str(l[1])+"\n")
           print(l[0]+" : " + str(l[1]))
        fileWriter.close()

        

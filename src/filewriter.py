import codecs 

class FileWriter:
    def __init__(self,pathToFile):
        self.pathToFile=pathToFile
        self.file =codecs.open(pathToFile,'w','utf-8')
    def write(self, strToWrite):
        self.file.write(strToWrite)
    def close(self):
        self.file.close()
import codecs
class FileReader:
    def __init__(self,pathToFile):
        self.pathToFile=pathToFile
    def open(self):
        self.file = codecs.open(self.pathToFile,'r','utf-8')
        return self.file
    def close(self):
        self.file.close()
import os.path
import pickle
import json

class UseWrite(Exception):
    pass
class FileNotFound(Exception):
    pass
class NoContent(Exception):
    pass


def createFile(filePath: str):
    try:
        open(filePath,"x")
    except:
        raise UseWrite("File already exists")

#deletes file
def delFile(filePath):
    if os.path.isfile(filePath) == True:
        os.remove(filePath)
    else:
        raise FileNotFound("file does not exist")


#note: 
#all created files will be overwritten when writeFile is used
class cache:

    #creates file
    def __init__(self, homeDir) -> None:
        self.homeDir = homeDir
        self.jsonCache = f"{homeDir}/cache.json"
        if not os.path.isfile(self.jsonCache):
            createFile(self.jsonCache)
    

    def readJsonCache(self):
        file = open(self.jsonCache,"r")
        fileContent = str(file.read())
        try:
            dictFormat = json.loads(fileContent)
            file.close()
            return dictFormat
        except json.JSONDecodeError:
            file.close()
            raise NoContent("no content in file")

    
    def writeJsonCache(self, content):
        file = open(self.jsonCache, "w")
        file.write(json.dumps(content, indent=4))
        file.close()

        
    def addToJson(self,instance: str,dir: str):
        try:
            dictFormat = self.readJsonCache()
            dictFormat.update({instance:dir})
            self.writeJsonCache(dictFormat)
        except NoContent:
            dictFormat = {instance:dir}
            self.writeJsonCache(dictFormat)
        
    
    def removeFromJson(self,instance: str):

        dictFormat = self.readJsonCache()
        del dictFormat[instance]
        self.writeJsonCache(dictFormat)

    def writeVar(self, var, instance):
        filePath = f"{self.homeDir}/{instance}.window"
        createFile(filePath)
        file = open(filePath, "wb")
        pickle.dump(var,file)
        file.close()
        self.addToJson(instance,filePath)

    def removeVar(self,instance):
        filePath = f"{self.homeDir}/{instance}.window"
        delFile(filePath)
        self.removeFromJson(instance)


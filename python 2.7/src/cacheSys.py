import os
import pickle
import json

#exceptions
class UseWrite(Exception):
    pass
class FileNotFound(Exception):
    pass
class NoContent(Exception):
    pass


#simple file operations with custom exceptions
def createFile(filePath):
    try:
        f = open(filePath,"w")
        f.close()
    except:
        raise UseWrite("File already exists")

def delFile(filePath):
    if os.path.isfile(filePath) == True:
        os.remove(filePath)
    else:
        raise FileNotFound("file does not exist")


#note: 
#created file will be overwritten when write is used

#a JSON file is created to store index of all cached instances (variables)
class cache:

    #creates file
    def __init__(self, homeDir, extension):
        self.homeDir = homeDir
        self.jsonCache = "{}/cacheStore.json".format(homeDir)
        if not os.path.isfile(self.jsonCache):
            createFile(self.jsonCache)
        
        self.extension = extension
    
    
    def readJsonCache(self):
        file = open(self.jsonCache,"r")
        fileContent = str(file.read())
        try:
            dictFormat = json.loads(fileContent)
            file.close()
            return dictFormat
        except ValueError:
            file.close()
            raise NoContent("no content in file")

        
    def addToJson(self,instance,dir):
        try:
            dictFormat = self.readJsonCache()
            dictFormat.update({instance:dir})
            self.writeJsonCache(dictFormat)
        except NoContent:
            dictFormat = {instance:dir}
            self.writeJsonCache(dictFormat)
        
    
    def removeFromJson(self,instance):

        dictFormat = self.readJsonCache()
        del dictFormat[instance]
        self.writeJsonCache(dictFormat)

    #write to the json file
    def writeJsonCache(self, content):
        file = open(self.jsonCache, "w")
        file.write(json.dumps(content, indent=4))
        file.close()


    #work with picked file formats (binary)
    #auto use JSON cache

    """
        if pickle is not used, python would only store a pointer to the variable in memory.
        pickle converts the value of the variable to binary format and stores it to a file 
        making sure that the variable will be read correctly and always available
    
    """
    def writeVar(self, var, instance):
        filePath = "{}/{}.{}".format(self.homeDir,instance,self.extension)
        createFile(filePath)
        file = open(filePath, "wb")
        pickle.dump(var,file)
        file.close()
        self.addToJson(instance,filePath)

    def removeVar(self,instance):
        filePath = "{}/{}.{}".format(self.homeDir,instance,self.extension)
        delFile(filePath)
        self.removeFromJson(instance)

    def readVar(self, instance):
        jsonCacheDict = self.readJsonCache()
        if instance in jsonCacheDict:
            filePath = "{}/{}.{}".format(self.homeDir,instance,self.extension)
            file = open(filePath, "rb") 
            value = pickle.load(file)
            return value


class layer:
    def __init__(self, coords):
        self.value = coords
    
    def readValue(self):
        return self.value



class layerMgr:

    def __init__(self):
        self.layerList = []
        self.layerDict = {}
        self.layerNpos = 0

    def setPos(self,layerName, Npos ):

        if layerName in self.layerList and Npos != None:
            self.layerList.insert(Npos, self.layerList.pop(self.layerList.index(layerName)))
        elif Npos != None:
            self.layerList.insert(Npos, layerName)
        else:
            self.layerList += [layerName]
            self.layerNpos += 1 

    def find(self, target):
        if type(target) == str:
            return self.layerList.index(target)
        elif type(target) == int:
            return self.layerList[target]
        else:
            raise ValueError("invalid variable type\nuse int or str")

    def addLayer(self, layerName, layer):
        self.layerDict.update({layerName: layer})
        self.setPos(layerName,None)

    def remove(self, target):
        if type(target) == str:
            self.layerList.remove(target)
        elif type(target) == int:
            del self.layerList[target]
        else:
            raise ValueError("invalid variable type\nuse int or str")
    
    def readValues(self,layer):
        tmp = []
        for x in self.layerDict[layer].value:
            tmp += [[x.value[0][0],x.value[0][1]]]
        return tmp
        








        

        
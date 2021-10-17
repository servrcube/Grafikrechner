class layer:
    def __init__(self, coords: list):
        self.value = coords



class layerMgr:

    def __init__(self) -> None:
        self.layerList = []
        self.layerDict = {}
        self.layerNpos = 0

    def setPos(self,layerName, Npos ):

        if layerName in self.layerList:
            self.layerList.insert(Npos, self.layerList.pop(self.layerList.index(layerName)))

    def find(self, target):
        if type(target) == str:
            return self.layerList.index(target)
        elif type(target) == int:
            return self.layerList[target]
        else:
            raise ValueError("invalid variable type\nuse int or str")
    

    def addLayer(self, layerName: str, layer : layer ):
        self.layerDict.update({layerName: layer})
        self.setPos(layerName,None)

    def remove(self, target):
        if type(target) == str:
            self.layerList.remove(target)
            self.layerDict.remove(target)
        elif type(target) == int:
            del self.layerDict[self.layerList[target]]
            del self.layerList[target]
        else:
            raise ValueError("invalid variable type\nuse int or str")







        

        
from layerMgr import layer, layerMgr
from plot import *
from cacheSys import *
from time import sleep
from inspect import getsource



class simplePlot:

    def __init__(self,height,width):
        #the size of a step of change in x
        self.dx = 0.01

        #dimentions of graph positive and negative axis following order: xmin,ymin,xmax,ymax
        self.winDim = matrix([[-height/2,-width/2],[height/2,width/2]])

        #basis vectors
        self.i_hat = [1,0]
        self.j_hat = [0,1]

        self.coords = coords(self.dx, self.winDim, matrix([self.i_hat, self.j_hat]))

        cacheFolder = "./cache/"
        extension = "window30"

        self.layers = layerMgr()

        if not os.path.exists(cacheFolder):
            os.mkdir(cacheFolder)
            sleep(1)


        self.cache = cache(cacheFolder,extension)


    
    def runFunction(self,func):
        if func.__name__ == "<lambda>":
            get_lambda_name = lambda l: getsource(l).split('=')[0].strip()
            name = get_lambda_name(func)
        else:    
            name = func.__name__
        coords = self.coords.runFunction(func)
        self.layers.addLayer(name,layer(coords)) 

    
    def getFunction(self,name):
        if type(name) != str:
            raise ValueError("please enter a string")
        return list(map(lambda x: x.value[0] ,self.layers.layerDict[name].value))

    def saveFunctions(self, name):
        self.cache.writeVar(self.layers,"save_"+name)

    def readFromCache(self,name):
        self.layers = self.cache.readVar("save_"+name)
    
    def listFunctions(self):
        return self.layers.layerList

        






import sys

sys.path.append("..\\grafikrechner\\python27")

from plot import *
from sys import getsizeof
from layerMgr import *
from math import *
from cacheSys import *

#beginnning programm


#init all vars

#the size of a step of change in x
dx = 0.01

#dimentions of graph positive and negative axis following order: xmin,xmax,ymin,ymax
winDim = matrix([[-10,-10],[10,10]])

#basis vectors
i_hat = [1,0]
j_hat = [0,1]

def line(x):
    return 1
def simple(x):
    y = x**2-4
    return y
def simple2(x):
    y = x*2-4
    return y
def breakingFunction(x):
    y = acosh(x)
    return y


if __name__ == "__main__":

    #create coordinate system
    coords = coords(dx, winDim, matrix([i_hat, j_hat]))

    #run functions
    cordinates = coords.runFunction(simple)

    #make a layer of the output coordinates
    layerSimple = layer(cordinates)

    layerSimple2  = layer(coords.runFunction(simple2))
    layerLine = layer(coords.runFunction(line))

    #to fix domain error used try:, except:
    layerBreakingFunction = layer(coords.runFunction(breakingFunction))

    #simple dot
    layerPoint = layer(coords.point(5,1))

    layers = layerMgr()

    layers.addLayer("simple", layerSimple)
    layers.addLayer("simple2", layerSimple2)
    layers.addLayer("line", layerLine)
    layers.addLayer("breakingFunction", layerBreakingFunction)


    #checking file size (variables)

    local_vars = list(locals().items())
    total = 0
    for var, obj in local_vars:
        total += sys.getsizeof(obj)

    #size of all vars
    print(total/1024,"kb")

    #store output

    cacheStore = cache("./cache","window30")

    cacheStore.writeVar(layers,"example")



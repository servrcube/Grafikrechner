from cacheSys import *
from matrix import *
from gturtle import *


#simple func from imported var for testing
def simple(x):
    y = (x**2)/104-4
    return y

if __name__ == "__main__":
    
    #set window size
    setPlaygroundSize(500, 500)  
    
    #use the stored cache (a folder)
    cache = cache("./cache","window")
    
    window = cache.readVar("example")  

    # make and hide the turtle (plotter)
    makeTurtle()
    hideTurtle()
    
    
    #plot my programm
    for n in window.readValues("simple"):
        penUp()
        #print(n.value[0][0],n.value[0][1])
        setPos(n)
        penDown()
        dot(1)
    
    
    #reference shifted by 2
    """
        the reference shows that my programm is a accurate representation of the function
        made nomally by a simple function

    """
    setPenColor("red")
    x = -500
    for n in range(1000*100):
            penUp()
            #print(x,simple(x))
            setPos(x+2,simple(x))
            penDown()
            dot(1)
            x += 0.01
    

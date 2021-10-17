plot
====

How to use
----------

Firstly we need to initialise the coords class

the coords class needs 3 things:

-  window dimentions
-  basis vectors
-  step size


import plot

.. code:: python

    from plot import *

set up the init variables

.. code:: python


    #the size of a step of change in x
    dx = 0.01

    #window dimentions are a 2x2 matrix
    #order: xmin,ymin,xmax,ymax
    winDim = matrix([[-500,-500],[500,500]])

    #basis vectors
    i_hat = [1,0]
    j_hat = [0,1]

    basisMat = matrix([i_hat,j_hat])

init coords

.. code:: python

    coords = coords(dx, winDim, basisMat)

you can pass lambda or def functions

.. code:: python


    simplefunction = lambda x: x+1

    def simplefunction2(x):
        return x+1

use runFunction to get the coordinates

.. code:: python


    simpleOutput = coords.runFunction(simpleFunction)
    simpleOutput2 = coords.runFunction(simpleFunction2)




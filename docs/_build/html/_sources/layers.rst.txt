layer manager
=============

How to use?
-----------

all coordinates form the plot function can be saved in a layer class

.. code:: python

    layer1 = layer(coordsoutput)

this layer can then be added to the layerMgr class

.. code:: python

    layers = layerMgr()
    layers.addLayer(layerName, layer1)

to read a layer by its value use the layerDict

.. code:: python
    
    layerOut = layers.layerDict[layerName]

to get the value use .value

.. code:: python

    layerOut.value

to remove a layer use remove

.. code:: python

    layers.remove(layerName)
    #also possible is the order you stored it in
    layers.remove(0)
    
to find the index of a layer and vica versa use find

.. code:: python

    layers.find(layerName)
    layers.find(0)

to change the position of the layer in the layerlist use setPos
(can be helpful to set render order) 

.. code:: python

    layers.setPos(layerName,pos)
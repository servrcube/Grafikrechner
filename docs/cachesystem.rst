cache system
============

What is cacheSys
----------------

Overview
~~~~~~~~

CacheSys is a module to save variables to a file, so that they can be
read by another program. All files are saved in a pickle format and indexed in a
cacheStore.json file in the cache folder.

What problems does this solve
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normally if you were to store a variable to a file directly,it would
only store a pointer to the variable, 
by pickling the variable you are able to store the individual values.

How to use cacheSys
-------------------

Remember to include the folder in your sys.path, `how
to? <quickstart.html#id1>`__

.. code:: python

    from cacheSys import *

    #use a directory for storing your variables
    cachePath "./path/to/your/cache/"
    #pick a extension (all files are stored in pickle format)
    extention = "example"

    #init the cache class
    cache = cache(cachePath, extention)

    yourVar = "your Value"

    #inststance name to store and access your variable
    instanceName = "exampleVar"

    #Note: you can store the same variable under diffrent instance names
    #but storing to the same instance name will overrite the instance

    #to store a variable
    cache.writeVar(yourVar,instance)

    #to read a variable
    valueOfCachedVar = cache.readVar(instance)

    #to delete a variable
    cache.removeVar(instance)

your cached variables will indexed in a JSON file called jsonStore.json
like this:

.. code:: json

    {
        "exampleVar": "./path/to/your/cache/exampleVar.example"
    }



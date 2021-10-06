#!/usr/bin/env python
# coding: utf-8

# In[246]:


#one nested list ist one column
x = [[1,0],[0,1]]
y = [[1,2],[1,6]]

#note to lists
"""
    using * to create size of list, actually just makes copies and not new instances:
    
    so if I do:
    x = [[0]*3]*3
    
    then:
    x[0,0] = 1
    the result is:
    [[1,0,0][1,0,0][1,0,0]]
    
    not:
    [[1,0,0][0,0,0][0,0,0]]

    to avoid this I used for:
    [[0 for y in range(n)] for x in range(n)]

"""
     
#gives dimementions of a list in format: [x,y]
def dim(x):
    prevLen = len(x[0])
    for i in x:
        currentLen = len(i)
        if currentLen != prevLen:
            raise IndexError('matrix is irregular make sure Row and Column lengths are the same')
            
        
    return len(x),len(x[0])

#gives dot product
def dot(a,b):
    dimA = len(a)
    dimB = len(b)

    if dimA != dimB: 
        raise ValueError("row and column lengths do not match")
    
    tmp = 0
    for matA,matB in zip(a,b):
        tmp += abs(matA) * abs(matB)
    
    return tmp
    
def add(a,b):
    
    dimA = dim(a)
    dimB = dim(b)

    if dimA != dimB: 
        raise ValueError("To add matrices, the matrices must have the same dimensions")
        
    tmp = []
    for x in range(dimA[0]):
        tmpInter = []
        for y in range(dimA[1]):
            tmpInter += [a[x][y] + b[x][y]]
        tmp += [tmpInter]
    
    return tmp

def sub(a,b):
    
    dimA = dim(a)
    dimB = dim(b)

    if dimA != dimB: 
        raise ValueError("To subtract matrices, the matrices must have the same dimensions")
        
    tmp = []
    for x in range(dimA[0]):
        tmpInter = []
        for y in range(dimA[1]):
            tmpInter += [a[x][y] + b[x][y]]
        tmp += [tmpInter]
    
    return tmp


def mult(a,b):
    
    if type(a) == int:
        tmp = []
        dimB = dim(b) 
        
        for x in range(dimB[0]):
            tmpInter = []
            for y in range(dimB[1]):
                tmpInter += [b[x][y] * a]
            tmp += [tmpInter]
        
        return tmp
                
    if type(b) == int:
        tmp = []
        dimA = dim(a) 
        
        for x in range(dimA[0]):
            tmpInter = []
            for y in range(dimA[1]):
                tmpInter += [a[x][y] * b]
            tmp += [tmpInter]

            
        return tmp
    
    dimA = dim(a)
    dimB = dim(b)
     
    tmpMat = [[0 for i in range(dimA[1])] for i in range(dimB[0])]
    
    for r in range(dimA[1]):
        
        tmpInter = []
        
        for n in range(dimA[0]):
            tmpInter += [a[n][r]]
            
        for p in range(dimA[1]):
            tmpMat[r][p] = dot(tmpInter,b[p])

    return tmpMat


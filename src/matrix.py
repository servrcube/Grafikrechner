#one nested list ist one column
# eg. x = [[1,0]<-col,[0,1]]<-matrix

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

#add two matricies    
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

#subtract two matricies
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

#multiply two matricies
def mult(a,b):
    
    # scalar matrix multiplication
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

    #matrix matrix multiplication
    
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

class matrix:
    def __init__(self,value):
        self.value = value
        self.dim = dim(value)
    
    def __add__(self,other):
        if type(other) != matrix:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other)}' and 'matrix'")
        return matrix(add(self.value,other.value))
    
    def __sub__(self,other):
        if type(other) != matrix:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other)}' and 'matrix'")
        return matrix(sub(self.value,other.value))
    
    def __mul__(self,other):
        if type(other) != matrix:
            raise TypeError(f"unsupported operand type(s) for *: '{type(other)}' and 'matrix'")
        return matrix(mult(self.value,other.value))
    
    def getRows(self):
        #converts the column -> list format to row -> list
        tmp = []
        for r in range(self.dim[1]):
            tmpInter = []
            for p in range(self.dim[0]):
                tmpInter += [self.value[p][r]]
            tmp += [tmpInter]
        return matrix(tmp)
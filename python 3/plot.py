from matrix import *


class WindowDimError(Exception):
    pass

#coordinate system
class coords:

    #init coords
    def __init__(self, dx, winDim: matrix, basis_vectors: matrix):
        
        #creates all variables
        self.dx = dx
        
        #defines limits
        self.xmin , self.xmax = winDim.getRows().value[0]
        self.ymin , self.ymax = winDim.getRows().value[1]

        #unit vectors
        self.basis_vectors = basis_vectors
        
        #checks limits of graph(s)
        if not (self.xmin < self.xmax and self.xmin <= 0 and self.xmax >= 0 and self.ymin <= self.ymax and self.ymin <= 0 and self.ymax >= 0):
            raise WindowDimError("\nplease check if \n xmin < xmax \n xmin < 0 \n xmax > 0 \n ymin < ymax \n ymin < 0 \n ymax > 0")
    
    def finalCoords(self,coordinates: matrix):
        x = self.basis_vectors
        tmp = []
        mult = coordinates.getRows().value
        return matrix([list(map(lambda a: sum(list(map(lambda n,p: n*p , a, mult[0] ))) ,x.getRows().value))])
    
    def inWindow(self, x,y):
        pass
    
    def localCoords(self, x,y):
        return self.finalCoords(matrix([[x],[y]]))
      
    
    def runFunction(self, func):
        #draws as per given function
        current_x = self.xmin
        tmp = []
        while current_x < self.xmax:
            
            try:
                current_y = func(current_x)
                if current_y <= self.ymax and current_y >= self.ymin:
                    tmp += [self.localCoords(current_x , current_y)]
                    
            except ValueError as error:
                if str(error) == "math domain error":
                    pass
                else:
                    raise Exception(error)
                    #exec(f"raise {error.__class__.__name__}(error)")"""

            current_x += self.dx
        return tmp
            
    def point(self, x,y):
        return self.localCoords(x,y)
        
            
    
        
        



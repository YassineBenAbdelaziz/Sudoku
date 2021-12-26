"""
The Solver class has the responsible methods for creating unique solution sukoku grid 
** __init__ : main constructor
** possible : returns True if x number possible to put in a certain cell according to sukoku rules.
** solve : solves a grid
** createFilledGrid : creates a filled sukoku grid according to sukoku rules
** clearGrid : remove numbers of a filled grid to obtain unique solution grid
"""

from copy import deepcopy
from random import shuffle

class Solver :


    def __init__(self) :
        self.counter = 0 
        self.numbers = [1,2,3,4,5,6,7,8,9]
        self.positions = list(range(0,81))
        self.grid = []
        self.solvedGrid = []
        self.emptyGrid = []
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.emptyGrid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])



    def possible(self,x,y,n,grid) :
        
        for j in range(9) :
            if grid[x][j] == n :
                return False

        for i in range(9) :
            if grid[i][y]  == n :
                return False

        x1 = (x // 3) * 3
        y1 = (y // 3) * 3

        for i in range (3) :
            for j in range(3) :
                if grid[x1+i][y1+j] == n :
                    return False

        return True



    def solve(self,grid) :
        if self.counter == 2 : 
            return
    
        for x in range(9) :
            for y in range(9) :
                if grid[x][y] == 0 :                
                    for n in range(1,10) :
                        if self.possible(x,y,n,grid) :
                            grid[x][y] = n 
                            self.solve(grid)
                            grid[x][y] = 0 

                    return 
        self.counter += 1
        






    def copyEmptyGrid(self) :
        self.grid = deepcopy(self.emptyGrid)


    def copySolvedGrid(self) :
        self.solvedGrid = deepcopy(self.grid)


    def createFilledGrid(self) :
         
        for x in range(9) :
            for y in range(9) :
                if self.grid[x][y] == 0 :                      
                    shuffle(self.numbers)         
                    for n in self.numbers :
                        if self.possible(x,y,n,self.grid) :
                            self.grid[x][y] = n 
                            found = self.createFilledGrid()
                            if not found :
                                self.grid[x][y] = 0 
                            else :
                                return True
                    return False
        
        return True



    def clearGrid(self):
        
        shuffle(self.positions)
        for p in self.positions :
            row = p // 9 
            col = p % 9
            backup = self.grid[row][col] 
            self.grid[row][col] = 0 
            self.counter = 0
            self.solve(self.grid)
            if  self.counter > 1  :
                self.grid[row][col] = backup
        


    def getGrid(self) :
        return self.grid


    def getSolvedGrid(self) :
        return self.solvedGrid



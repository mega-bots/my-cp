"""
LEET CODE UNIQUE PATH III
"""
#UNIQUE PATHS
class Solution:
    def Print(self,matrix):
        for i in matrix:
            print(i)
    def isvalid(self,currrow,currcol,grid,boolarr,rows,col):
        return (currrow>=0 and currrow<rows and currcol>=0 and currcol<col) and boolarr[currrow][currcol]==0 and grid[currrow][currcol]==0
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    def solve(self,currrow,currcol,finalrow,finalcol,grid,rows,column,boolarr):
        print((currrow,currcol),end = " ")
        if (currrow == finalrow and currcol == finalcol):
            for i in boolarr:
                if 0 in i:
                    return 0
            
            return 1
        count=0
        for row,col in self.moves:
            currrow+=row
            currcol+=col
            if self.isvalid(currrow,currcol,grid,boolarr,rows,column):
                boolarr[currrow][currcol]=1
                count+=self.solve(currrow,currcol,finalrow,finalcol,grid,rows,column,boolarr)
                boolarr[currrow][currcol]=0
            currrow-=row
            currcol-=col
        return count
                
    def uniquePathsIII(self, grid):
        rows = len(grid)
        col = len(grid[0])
        boolarr = grid
        for index,i in enumerate(grid):
            if 2 in i:
                finalrow = index
                finalcol = i.index(2)
        return self.solve(0,0,finalrow,finalcol,grid,rows,col,boolarr)
        
        
a = Solution()
print(a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))

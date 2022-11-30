# function to print grid
def printGrid(grid):
    for x in grid:
        for y in x:
            print(y,end=" ")
        print()
# function to check if the value to be assigned to a cell already exists in that row of that cell
# it returns true if 'val' can be placed in a cell with row number as 'row'
def rowCheck(grid,row,val):
    #iterate through that row
    for j in range(9):
        # if value to be assigned is found then 
        # it can't be placed in that cell
        if val==grid[row][j]:
            return False
    return True

# function to check if the value to be assigned to a cell already exists in that column of that cell
# it returns true if 'val' can be placed in a cell with column number as 'col'
def colCheck(grid,col,val):
    #iterate through that column
    for i in range(9):
        # if value to be assigned is found then 
        # it can't be placed in that cell
        if val==grid[i][col]:
            return False
    return True
#function to check "box" condition
def boxCheck(grid,row,col,val):
    # get the center cell(r,c) of the box 
    # with simple formula below
    r=(row//3)*3+1
    c=(col//3)*3+1
    # iterate through each cell of the box
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            # for each cell of the box check if the value to be placed exists
            # if exits then it can't be placed in that cell
            if grid[r+i][c+j]==val:
                return False
    return True

# function to find unassigned cell(a cell which doesn't contain a value) in the grid
def findUnassigned(grid):
    for i in range(9):
        for j in range(9):
            # cell which contains dot(.) is unassigned
            if grid[i][j]==0:
                return i,j
    # if no cell left unassigned
    return -1,-1

# function to complete the sudoku
def sudokuSolver(grid):
    # find an unassigned cell in the grid
    i,j=findUnassigned(grid)
    # if no cell remain unassigned then the grid is filled completely and is valid
    if i==-1 and j==-1:
        return True

    # for each 'num' ranging from 1 to 9 check if it can be placed at '(i,j)'
    for num in range(1,10):
        # 'num' can be placed at '(i,j)' if 
        # any value in row 'i' is not equal to 'num'
        # any value in column 'j' is not equal to 'num'
        # any value in the box it belongs to is not equal to 'num'
        if rowCheck(grid,i,num) and colCheck(grid,j,num) and boxCheck(grid,i,j,num):
            #all the conditions are satisfied

            #place 'num' at '(i,j)' temporarily
            grid[i][j]=num
            
            #check for the next cells
            if sudokuSolver(grid):
                return True

            # we've reached here because the choice we made by putting some 'num' here was wrong 
            # hence now leave the cell unassigned to try another possibilities 
            grid[i][j]=0
    #  putting any value doesn't solve the grid that means we've made a wrong choice earlier
    #  if no value can be placed at '(i,j)' then returns false meaning that the current
    #  sudoku is not feasible and try for another possibilities
    return False

grid  = [[4,0,6,0,0,0,0,0,8],
         [0,3,5,0,0,2,9,4,0],
         [0,8,0,4,0,0,0,1,6],
         [0,4,0,9,0,8,7,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,2,6,0,1,0,5,0],
         [2,5,0,0,0,1,0,5,0],
         [0,9,3,1,0,0,6,2,0],
         [6,0,0,0,0,0,4,0,3]]

if sudokuSolver(grid):
    printGrid(grid)
else:
    print("No solution exists!")

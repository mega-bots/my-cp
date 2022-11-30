#program to solve rat in a maze
#n = int(input("enter the size of the maze "))
n=5
board = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [1, 1, 1, 0, 1],
         [1, 0, 0, 0, 1]]
new_board= [[0]*n for i in range(n)]
move_x=[1,-1,0,0]
move_y=[0,0,1,-1]
def isvalid(row,col):
    return (row<n and col<n and row>=0 and col>=0)
def display(board):
    for i in board:
        for j in i:
            print(j,end = " ")
        print("")
    print("\n")
display(board)

def solve(row,col,board):
     if row==n-1 and col==n-1:
        display(new_board)
        return True
     for i in range(4):
         new_x,new_y = row+move_x[i],col+move_y[i]
         if isvalid(new_x,new_y):
          #print(new_x,new_y)
          if board[new_x][new_y]==1 and new_board[new_x][new_y]==0:
            new_board[new_x][new_y]=1
            solve(new_x,new_y,board)
            new_board[new_x][new_y]=0
            
    
solve(0,0,board)

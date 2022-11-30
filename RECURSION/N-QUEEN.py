#program to solve N-Queen puzzle
n = int(input("enter the size of the board "))
board = [['.']*n for i in range(n)]
state = [[0]*n for i in range(n)]
leftrow=[0]*n
updiag=[0]*(2*n-1)
lowdiag=[0]*(2*n-1)
def display(board):
    for i in board:
        for j in i:
            print(j,end = " ")
        print("")
    print("\n")
display(board)
def solve(col,row,arr,board,state):
    if (col==n):
        display(board)
        return
    for row in range(n):
      if not (row>=n or col>=n or row<0 or col<0 or leftrow[row]==1 or updiag[row+col]==1 or lowdiag[n-1+col-row]==1):
        board[row][col]='Q'
        state[row][col]=1
        leftrow[row]=1
        updiag[row+col]=1
        lowdiag[n-1+col-row]=1
        solve(col+1,row,arr,board,state)
        leftrow[row]=0
        updiag[row+col]=0
        lowdiag[n-1+col-row]=0
        board[row][col]='.'
        state[row][col]=0
solve(0,0,[],board,state)





        
        

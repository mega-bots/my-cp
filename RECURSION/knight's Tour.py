#program to solve knights tour problem
N = int(input())
board = [[0]*N for i in range(N)]
move_x = [ -2, -1, 1, 2,2, 1, -1, -2]
move_y = [ -1, -2, -2, -1,1, 2, 2, 1]
def moves(row,col):
    return [(row+2,col+1),(row+1,col+2),(row+1,col-2),(row+2,col-1),(row-2,col+1),(row-1,col+2),(row-2,col-1),(row-1,col-2),(row+2,col+1),(row+1,col+2),(row+1,col-2),(row+2,col-1)]
def isvalid(row,col):
      return (row<N and col<N and row>=0 and col>=0 and board[row][col]==0)
def display(board):
    for i in board:
        for j in i:
            print(j,end = " ")
        print("")
    print("\n")
display(board)
def solve(Row,Col,arr,board,count):
  if (count==N*N+1):
          display(board[:])
          return True
  for i in range(8):
      #row,col=moves(Row,Col)[i]
      row,col=Row+move_x[i],Col+move_y[i]
      if (isvalid(row,col)):
            board[row][col]=count
            count=count+1
            if solve(row,col,arr,board,count):
                return True
            count=count-1
            board[row][col]=0
  return False
board[0][0]=1
solve(0,0,[],board,2)

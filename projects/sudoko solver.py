import os
os.rename(__file__,"sudoko solver.py")
class Solution:
    def isvalid(self,num,row,col,board):
        if num in board[row]:
            return False
        for i in range(3):
            for j in range(3):
                if board[3*(row//3)+i][3*(col//3)+j] == num:
                    return False
        for i in board:
            if i[col]==num:
                return False
        return True
    def solve(self,Row,Col,n,board):
        if Row==n-1 and Col == n-1:
            print(board)
            return 0
        for row in range(n):
            for col in range(n):
                if board[row][col]=='.':
                    for num in range(1,10):
                        if self.isvalid(str(num),row,col,board):
                            board[row][col]=str(num)
                            self.solve(row,col,n,board)
                            board[row][col]='.'
    def solveSudoku(self,board):
        self.solve(0,0,len(board),board)
a = Solution()
a.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
        

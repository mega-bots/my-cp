"""
#permutations

s = input()
def permutations(ind,arr,n,s,matrix):
    if ind==n:
        print("".join(arr))
        return
    for i in range(n):
        if matrix[i]==0:
            matrix[i]=1
            permutations(ind+1,arr+[s[i]],n,s,matrix)
            matrix[i]=0
#permutations(0,[],len(s),s,[0]*len(s))


#combinations
s = input("enter a string ")
def combinations(ind,arr,n,s):
    if ind==n:
        print("".join(arr))
        return
    for i in range(len(s)):
        
            combinations(ind+1,arr+[s[i]],n,s)

combinations(0,[],int(input("enter the number of combinations ")),s)

#subsets
s = input()
def subset(ind,n,arr,s):
    if ind==n:
        print("".join(arr))
        return 
    subset(ind+1,n,arr+[s[ind]],s)
    subset(ind+1,n,arr,s)
    
subset(0,len(s),[],s)


#target sum use only once
lis = [1,2,3,4,5,6]
s = int(input())
def solve(ind,n,target,arr,lis):
    if ind==n:
        if target==0:
            print(arr)
        return
    if target<0:
        return
    if target==0:
        print(arr)
        return
    solve(ind+1,n,target-lis[ind],arr+[lis[ind]],lis)
    solve(ind+1,n,target,arr,lis)
solve(0,len(lis),s,[],lis)


#target sum using many times
lis = [6,9,10]
s = int(input())
def solve(target,arr,lis):
    if target==0:
        print(arr)
        return
    if target<0:
        return
    for i in lis:
        solve(target-i,arr+[i],lis)
solve(s,[],lis)


#target sum using many times without permutations
lis = [1,2,3,4,5]
s = int(input())
def solve(target,arr,lis,n):
    if target==0:
        print(arr[1:])
        return
    if target<0:
        return
    for i in range(n):
        if target-lis[i]<0:
            break
        if lis[i]>=arr[-1]:
          solve(target-lis[i],arr+[lis[i]],lis,n)
solve(s,[0],sorted(lis),len(lis))

"""


#rat in a maze challenge print all the possible ways
n=int(input("enter the size of the maze "))
print("enter the maze ")
board = [list(map(int,input().split())) for i in range(n)]
board1 = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [1, 1, 1, 0, 1],
         [1, 0, 0, 0, 1]]
check_board = [[0]*n for i in range(n)]
def moves(cur_x,cur_y):
    return [(cur_x+1,cur_y),(cur_x-1,cur_y),(cur_x,cur_y+1),(cur_x,cur_y-1)]
def print_b(board):
    #board[0][0]='A'
    #board[len(board)-1][len(board)-1]='B'
    for i in board:
        for j in i:
            print(j,end = " ")
        print(" ")
def is_valid(x,y,n):
    return x>=0 and y>=0 and x<n and y<n
def solve(cur_x,cur_y,fin_x,fin_y,check_board,board):
    if cur_x==fin_x and cur_y==fin_y:
        print_b(check_board)
        print("\n")
        return
    for i,j in moves(cur_x,cur_y):
        if is_valid(i,j,n) and check_board[i][j]==0 and board[i][j]==1:
            #check_board[cur_x][cur_y]=1
            check_board[i][j]=1
            solve(i,j,fin_x,fin_y,check_board,board)
            check_board[i][j]=0
            #check_board[cur_x][cur_y]=0
solve(0,0,n-1,n-1,check_board,board)
            
            
        
        
    














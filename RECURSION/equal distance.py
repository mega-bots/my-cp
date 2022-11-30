"""
Input: n = 3
Output:
3 1 2 1 3 2
2 3 1 2 1 3
 
Input: n = 4
Output:
4 1 3 1 2 4 3 2
2 3 4 2 1 3 1 4
"""
import os
os.rename(__file__,"equal distance.py")
#equal distance using recursion
n = int(input("enter a number: "))
c=1
memo = []
def solve(ind,arr,n,lis,memo):
    if 0 not in arr and arr not in memo:
        memo.append(arr[:])
        print(arr,ind)
    
    if ind<n and arr[ind]!=0:
        solve(ind+1,arr,n,lis,memo)
    for index,i in enumerate(lis):
        if lis[index]!=0:
         
         if arr[ind]==0 and ind+i+1<n and arr[ind+i+1]==0:
    
          arr[ind],arr[ind+i+1] = i,i
          lis[index]=0
          
          solve(ind+1,arr,n,lis,memo)  #backtrack
          
          arr[ind],arr[ind+i+1] = 0,0
          lis[index]=i
        
            
        
    
solve(0,[0]*2*n,2*n,list(range(1,n+1)),[])
    

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
n = int(input("enter a number: "))
c=1
memo = []
def solve(ind,arr,n,lis,memo):
    if 0 not in arr and arr not in memo:
      memo.append(arr[:])
      print(arr)
    
    for index,i in enumerate(lis):
        if lis[index]!=0:
          if ind+i+1>=n:
              return 0
          if arr[ind]==0 and arr[ind+i+1]!=0:
              continue
          check=0
          if arr[ind]==0 and arr[ind+i+1]==0:
            arr[ind],arr[ind+i+1] = i,i
            lis[index]=0
            check=1

          solve(ind+1,arr,n,lis,memo)
          if check:
            arr[ind],arr[ind+i+1] = 0,0
            lis[index]=i
            
        
    
solve(0,[0]*2*n,2*n,list(range(1,n+1)),[])
    

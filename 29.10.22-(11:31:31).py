def solve(ind,arr,lis,k,n):
    if ind>=k :
        print(lis)
        return 0
    for i in range(1,n+1):
      #if lis == [] or arr[i-1]>=lis[-1]:
        solve(ind+1,arr,lis+[arr[i-1]],k,n)

arr = [7,2,1,1,1]
k=2
solve(0,arr,[],k,len(arr))

def jumps(ind,n,prev,lis,arr):
        print(arr,ind)
        if ind==n-1:
            print(arr)
            return 1
        if ind>=n:
            return 0
        #base case 
        if lis[ind]+prev==lis[ind+1]:
            if jumps(ind+1,n,prev,lis,arr+[prev]):
                return 1
        if ind>0 and lis[ind]+prev+1 == lis[ind+prev-1]:
            if jumps(ind+prev-1,n,prev+1,lis,arr+[prev+1]):
                return 1
        return 0
stones = [0,1,3,5,6,8,12,17]
print(jumps(0,len(stones),1,stones,[]))

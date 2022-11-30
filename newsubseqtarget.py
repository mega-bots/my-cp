lis = sorted([1,1,2,3,2,4])
target = 4
N = len(lis)
def solve(ind,lis,storage,target):
    if target==0:
        print(storage)
        return 1
    if ind >= N or target<0:
        return 0
    for i in range(ind,N):
        if lis[i]!=-1:
            val = lis[i]
            lis[i]=-1
            found = solve(i+1,lis,storage+[val],target-val)
            if found and storage!=[]:
                return 1
            lis[i] = val
                    
    return 0
    
solve(0,lis,[],target)
            
    

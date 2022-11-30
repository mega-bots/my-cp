"""
program to find the possible combinations of numbers
to form a sum of k, where duplicate combinations are not allowed
"""
lis = input("enter the sequence :").split()
size = len(lis)
val = int(input("enter k value :"))
ans=[]
def combinations(ind,arr,target):
    if (target==0):
        val = sorted(list(map(int,arr)))
        if (val not in ans):
            ans.append(val)
            
        return
    for i in range(ind,size):
        if (i>ind and lis[i]==lis[i-1]):
            continue
        if (int(lis[i])>target):
            break
        arr.append(lis[i])
        combinations(i+1,arr,target-int(lis[i]))
        arr.pop()
combinations(0,[],val)
print(ans)

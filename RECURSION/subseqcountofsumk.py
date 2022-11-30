"""
pick or not pick// take or not take a value 
"""

#program to count the total subsequences whose sum is k
lis = input("enter the subsequence ").split()
size = len(lis)
val = int(input("enter the k value "))
def subseqcount(ind,summ):
    if (ind>=size):
        if (summ==val):
            return 1
        return 0
    summ+=int(lis[ind])
    l = subseqcount(ind+1,summ)
    summ-=int(lis[ind])
    r = subseqcount(ind+1,summ)
    return l+r
print(f"total subsequences with sum of {val} are: ",subseqcount(0,0))

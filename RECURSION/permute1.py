#program to print all permutations of a string
from time import time as t
lis = input().split()
size = len(lis)
tot = []
def permute(ind,arr):
    if (ind>=size):
        print("".join(lis))
        return
    for i in range(ind,size):
        lis[i],lis[ind]=lis[ind],lis[i]
        permute(ind+1,arr)
        lis[i],lis[ind]=lis[ind],lis[i]
t1 = t()
permute(0,[])
print(t()-t1)

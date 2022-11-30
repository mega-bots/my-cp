#program to print all permutations of a string
from time import time as t
lis = input().split()
size = len(lis)
tot = []
def permute(ind,arr,hashmap):
    if (ind>=size):
        print("".join(arr))
        return
    for i in range(size):
      if (hashmap[i]!=1):
        arr.append(lis[i])
        hashmap[i]=1
        permute(ind+1,arr,hashmap)
        hashmap[i]=0
        arr.pop()
t1 = t()
permute(0,[],[0]*size)
print(t()-t1)
   

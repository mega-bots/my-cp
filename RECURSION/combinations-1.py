"""
program to find the possible combinations of numbers
which can be used multiple times to form a sum of k
"""

arr = [1,2,3,1]
target = int(input("enter a number: "))
def generate(ind,n,target,arr,storage):
    if (ind ==n):
        if target==0:
            print(storage)
        return 0
    if arr[ind]<=target:
      generate(ind,n,target-arr[ind],arr,storage+[arr[ind]])
    generate(ind+1,n,target,arr,storage)
generate(0,len(set(arr)),target,list(set(arr)),[])


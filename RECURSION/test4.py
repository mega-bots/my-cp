#subset
inp = input("enter the sequence ").split()
size = len(inp)
k = int(input("enter k value "))
def subset(ind,arr,target):
    if (ind==size):
      if target==0:
        print("".join(arr))
      return
    arr.append(inp[ind])
    subset(ind+1,arr,target-int(inp[ind]))
    arr.pop()
    subset(ind+1,arr,target)
subset(0,[],k)


candidates=[2,3,6,7]
ans=[]
def combinations(ind,arr,target):
    if (ind==len(candidates)):
      if target==0:
          ans.append(arr[:])
      return 
    if (candidates[ind]<=target):
        arr.append(candidates[ind])
        combinations(ind,arr,target-candidates[ind])
        arr.pop()
    combinations(ind+1,arr,target)
combinations(0,[],7)
print(ans)

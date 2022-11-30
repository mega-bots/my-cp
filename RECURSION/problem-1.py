arr = list(map(int,input().split()))
target = int(input())
def generate(arr,target,structure,N):
    if target<0:
        return
    if (target==0):
        print(" ".join(map(str,structure)))
        return
    for i in arr:
        structure.append(i)
        generate(arr,target-i,structure,N)
        structure.pop()
generate(arr,target,[],len(arr))

dp = [0]*len(arr)
for i in range(len(arr)):
    if target>0:
        
    


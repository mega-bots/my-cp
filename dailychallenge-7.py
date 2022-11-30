"""
https://www.codingninjas.com/codestudio/problem-details/subset-sum-equal-to-k_1550954
"""
import random
#subset sum equals to k
arr = [1,2,3,4,5]
k = 12
n = len(arr)
def solve(ind,arr,target,memo):
    if target==0:
        return 1
    if ind==0:
        return arr[0]==target
    if (ind,target) in memo:
        return memo[(ind,target)]
    notpick = solve(ind-1,arr,target,memo)
    pick = 0
    if arr[ind]<=target:
        pick = solve(ind-1,arr,target-arr[ind],memo)
    if (ind,target) not in memo:
        memo[(ind,target)]=pick or not pick
    return pick or notpick
print("output",solve(n-1,arr,k,{}))

dp = [[0]*(k+1) for i in range(n)]
for i in range(n):
    dp[i][0]=1
dp[0][arr[0]]=1
target = k
for i in range(1,n):
    for j in range(1,target+1):
        notpick = dp[i-1][j]
        pick = 0
        if arr[i]<=j:
            pick = dp[i-1][j-arr[i]]
        dp[i][j]=pick or notpick

print(dp[-1][-1])







    

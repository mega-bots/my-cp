val = [10,30,20]
wt = [5,10,15]
W = 100
def solve(ind,wt,val,W):
    if ind==0:
        if wt[0]<=W:
            return val[0]
        else:
            return 0
    pick = -1e9
    if (wt[ind]<=W):
        pick = val[ind]+solve(ind,wt,val,W-wt[ind])
    notpick = solve(ind-1,wt,val,W)
    return max(pick,notpick)
    
n = len(val)
print(solve(n-1,wt,val,W))
dp = [[0]*(W+1) for i in range(n)]
for i in range(W+1):
    if wt[0]<=i:
      dp[0][i]=val[0]
    else:
      dp[0][i]=0
for i in range(1,n):
    for j in range(W+1):
        pick = -1e9
        if (wt[i]<=j):
            pick = val[i]+dp[i][j-wt[i]]
        notpick = dp[i-1][j]
        dp[i][j]=max(pick,notpick)
print(dp[-1][-1])
        
    









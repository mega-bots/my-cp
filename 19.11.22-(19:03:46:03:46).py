def solve(ind,n):
    if ind<0:
        return 1
    single = solve(ind-1,n)
    double = 0
    if (ind>=1 and 1<=int(n[ind-1]+n[ind])<=26):
        double =  solve(ind-2,n)
    return double+single
n = input()
size = len(n)
print(solve(size-1,n))
    
dp = [0]*(size+1)
dp[0]=1
for ind in range(1,size+1):
    single = dp[ind-1]
    double = 0
    if (ind>=2 and 1<=int(n[ind-2]+n[ind-1])<=26):
        double = dp[ind-2]
    dp[ind] = single+double
print(dp[-1])
    
    

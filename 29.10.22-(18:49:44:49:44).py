#frog jump with 1 and 2 steps
def tot_jumps(ind,memo):
    if ind<=1:
        return ind
    if ind not in memo:
      memo[ind]=tot_jumps(ind-1,memo)+tot_jumps(ind-2,memo)*(ind>1)
    return memo[ind]
n = int(input("enter the number of stairs: "))
# print(tot_jumps(n,{}))

#dynamic programming
dp = [0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[-1])

#space optimization
a = 0
b = 1
for i in range(2,n+1):
    c = a+b
    a = b
    b = c
print(c)
    
    


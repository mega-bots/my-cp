#program to count the total ways in which a number can be formed using 1,3,5
import time
n = int(input())
def generate(n,memo):
    if n==0:
        return 1
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    else:
      memo[n]=generate(n-1,memo)+generate(n-3,memo)+generate(n-5,memo)
    return memo[n]
#print(generate(n,{}))

dp = [1]+[0]*n
for i in range(1,n+1):
        dp[i]+=dp[i-1]+dp[i-3]*(i>2)+dp[i-5]*(i>4)
print(dp[-1])

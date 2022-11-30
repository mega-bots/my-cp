"""
https://www.codechef.com/submit/BINARYSUB
"""
#BINARY SUB

s = input("enter the string " )
S = {'a','b','ab','ba'}
def solve(ind,n,S,string,memo):
    if ind>=n:
        return 1
    if string[ind:] in memo:
        return memo[string[ind:]]
    c1=solve(ind+1,n,S,string,memo) #pick
    c2=0
    if ind+1<n and (string[ind:ind+2] in S):
        c2=solve(ind+2,n,S,string,memo)
    memo[string[ind:]]=c1+c2
    return c1+c2
print(solve(0,len(s),S,s,{}))

def solve1(ind,S,string):
    if (ind<=0):
        return 1
    c1=solve1(ind-1,S,string)
    c2=0
    if (ind-1>=0) and (string[ind-1:ind+1] in S):
        c2=solve1(ind-2,S,string)
    return c1+c2
print(solve1(len(s)-1,S,s))


N = len(s)
dp = [0]*N
dp[0]=1
for i in range(1,N):
    c1=dp[i-1]
    c2=0
    if (s[i-1:i+1] in S):
          if i-2<0:
              c2=1
          else:
            c2=dp[i-2]
    dp[i]=c1+c2

print (dp[-1])
    

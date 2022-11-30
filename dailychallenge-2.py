"""
https://www.codechef.com/submit/COUNTPART?tab=statement
"""
#count partitios
def solve(ind,lis):
    if ind<=0:
        return 1
    maxval = lis[ind]
    c=1
    count=0
    for i in range(ind,-1,-1):
        if i==ind or lis[i]>maxval or lis[i]<lis[i+1]:
            count+=solve(ind-c,lis)
        c+=1
        if lis[i]>maxval:
            maxval =lis[i]
    return count
lis = [1,2,3,4]
print(solve(len(lis)-1,lis))

dp = [0]*len(lis)
dp[0]=1
for i in range(1,len(lis)):
    maxval=lis[i]
    c=1
    count=0
    for j in range(i,-1,-1):
        if j==i or lis[j]>maxval or lis[j]<lis[j+1]:
            if i-c<=0:
                count+=1
            else:
              count+=dp[i-c]
        c+=1
        if lis[j]>maxval:
            maxval = lis[j]
    dp[i]=count
print(dp[-1])


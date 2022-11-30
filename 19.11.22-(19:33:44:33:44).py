import random
n = input()
#n = str(random.randint(10**1000,10**4000))
#print(n,"\n\n\n")
while(n!='0'):
            size = len(n)
            dp = [0]*(size+1)
            dp[0]=1
            for ind in range(1,size+1):
                single = 0
                if n[ind-1]!='0':
                  single = dp[ind-1]
                double = 0
                if (ind>=2 and n[ind-2]!='0' and 1<=int(n[ind-2]+n[ind-1])<=26):
                    double = dp[ind-2]
                dp[ind] = single+double
            print(dp[-1])
            n = input()

#CODECHEF SOLUTION

def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return 1
    else:
        return 0

for _ in range(int(input())):
    n,q = map(int,input().split())
    lis = list(map(int,input().split()))
    mainlis = {}
    
    
    
    
    
    
    
    for i in range(q):
      k,L1,R1,L2,R2 = map(int,input().split())
      k+=1
      count = 0
      if k not in mainlis:
        kthsetlist = [isKthBitSet(i,k) for i in lis]
        print(kthsetlist)
        zeroes = kthsetlist.count(0)
        ones = n - zeroes
        zeroesright = []
        onesright = []
        zerc = 0
        onec = 0
        for z in range(n):
            if kthsetlist[z]==0:
              zerc+=1
            else:
              onec+=1
            zeroesright.append(zeroes-zerc)
            onesright.append(ones-onec)
        print(zeroesright,onesright)
        mainlis[k]=[kthsetlist,zeroesright,onesright]
        #print(mainlisis[k])
        for j in range(L1-1,R1+1-1):
            if kthsetlist[j]==1:
              if L2!=R2:
                count+=zeroesright[L2-2]-zeroesright[R2-1]
              else:
                  count+=kthsetlist[L2-1]==0
            else:
              if L2!=R2:
                count+=onesright[L2-2]-onesright[R2-1]
              else:
                  count+=kthsetlist[L2-1]==1
        print(count)
      else:
          kthsetlist,zeroesright,onesright=mainlis[k]
          for j in range(L1-1,R1+1-1):
            if kthsetlist[j]==1:
              if L2!=R2:
                count+=zeroesright[L2-2]-zeroesright[R2-1]
              else:
                  count+=kthsetlist[L2-1]==0
            else:
              if L2!=R2:
                count+=onesright[L2-2]-onesright[R2-1]
              else:
                  count+=kthsetlist[L2-1]==1
          print(count)
          
      
          
      

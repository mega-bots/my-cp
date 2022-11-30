#CODECHEF SOLUTION
from math import log,ceil
def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return 1
    else:
        return 0

for _ in range(int(input())):
    n,q = map(int,input().split())
    lis = list(map(int,input().split()))
    mainlis = {}
    maxx = max(lis)
    
    forwardlis = []
    backwardlis = []
    for bit in range(1,ceil(log(maxx,2))+1+1):
      zeroesright = []
      zeroesleft = []
      onesright = []
      onesleft = []
      
      zeroc = 0
      onec = 0
      kthsetlist = [isKthBitSet(i,bit) for i in lis]
      totones = kthsetlist.count(1)
      totzeroes = n - totones
      for i in range(n):
        if isKthBitSet(lis[i],bit)==1:
            onec+=1
        else:
            zeroc+=1
        zeroesleft.append(zeroc)
        zeroesright.append(totzeroes-zeroc)
        onesright.append(totones-onec)
        onesleft.append(onec)
      print("kthsetlist=",kthsetlist)
      print("onesleft=",onesleft)
      print("onesright=",onesright)
      print("zeroesleft=",zeroesleft)
      print("zeroesright=",zeroesright)
      iterator = 0
      
      size = n-1
      while(iterator<n):
        tempfor = []
        tempback = []
        for move in range(n):
          tempfor.append(zeroesleft[iterator]*onesright[size-move-1]+onesleft[iterator]*zeroesright[size-move-1])
          tempback.append(zeroesright[iterator-1]*onesleft[size-move]+onesright[iterator-1]*zeroesleft[size-move])
        iterator+=1
        forwardlis.append(tempfor)
        backwardlis.append(tempback)
      print(tempfor,tempback)
    
    for query in range(q):
         k,L1,R1,L2,R2 = map(int,input().split())
         print(forwardlis[k][R1-2]-forwardlis[k][L1-1]+(backwardlis[k][L2-2]-backwardlis[k][R2-1]))
      
    
    
    
    
  

import random
for _ in  range(int(input())):
    #n = int(input())
    #lis = list(map(int,input().split()))
    n = random.randint(1,10)
    lis = random.sample(list(range(10))*10,n)
    print(lis)
    if n<=2:
        print("YES")
        continue
    i=0
    j=n-1
    if lis[i]==lis[j] or lis[i]==lis[j-1] or lis[i+1]==lis[j]:
        print("YES")
    else:
        while(i<j and lis[i]==lis[i+1]):
            i+=1
        while(j>i and lis[j]==lis[j-1]):
            j-=1
        if lis[i]==lis[j-1] or lis[i+1]==lis[j] :
            print("YES")
        else:
            print("NO")
            

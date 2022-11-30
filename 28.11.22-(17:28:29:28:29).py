for _ in range(int(input())):
    s = input()
    k = int(input())
    minn = float('inf')
    minind = 0
    lis = [0]*(k+1)
    pointer = 0
    for i in range(k+1):
        if s[i]!='0' and int(s[i])<minn:
            minind = i
            minn = int(s[minind])
    lis[pointer] = minind
    k = minind
    length = k
    while(k>=0):
        minn = s[minind];
        for i in range(minind+1,length+1):
            if (int(s[i])<= minn):
                minind = i;
                minn = int(s[minind])
        pointer+=1
        if (pointer<length):
          lis[pointer]=minind
        k-=minind
    for i in lis:
        print(s[i],end = " ")
    #print(s[len(lis):])
    
    

target = 9
lis = [1,2,3,4,5]
i=0
j = len(lis)-1
while(i<j):
    val = lis[i]+lis[j]
    if val==target:
        print(True)
        break
    elif val<target:
        i+=1
    else:
        j-=1
    
else:
    print(False)

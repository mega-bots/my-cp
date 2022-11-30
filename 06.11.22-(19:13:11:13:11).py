lis = [4,7,2,3,9,-4,-2,-7,-1,-5]
nearest = -float('inf')
num = 100
minn = float('inf')
for i in range(len(lis)):
    if lis[i]>num:
        nearest = [lis[i],min(lis[i],nearest)][nearest!=-float('inf')]
    minn = min(lis[i],minn)
print([nearest,['no element found',minn][num<minn]][nearest==-float('inf')])

#ugly numbers
n = int(input())
def nth_num(start,n):
    if start==n:
        return 0
    
    count=0
    while(count<=n):
      val = start ==1 or start%2==0 or start%3==0 or start%5==0
      count+=val+nth_num(start+val,n+(1-start ==1 or start%2==0 or start%3==0 or start%5==0))
    return count


    
print(nth_num(1,n))

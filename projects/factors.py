'''
 UPTO ~10^15 Try: 1000000000000000
Min time took 3.6 and Max time took 5.4 for computing 10^15(tested 10 times). UPVOTE 
'''
import time
n=int(input("enter a number: " ))
t1=time.time()
a=[i for i in range(1,int(n**(1/2)+1)) if n%i == 0]
if a[-1]**2 == n:
  z=-2
else:
  z=-1
print(a+[n//i for i in a[z::-1]])
print("\ntime taken is ",time.time()-t1)


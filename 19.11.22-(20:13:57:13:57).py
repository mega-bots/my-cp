from math import floor,sqrt as sq
def seive(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):
		if (prime[p] == True):
			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1
	lis = []
	for p in range(2, num+1):
		if prime[p]:
			lis.append(p)
	return lis
for _ in range(int(input())):
  m,n = map(int,input().split())
  primes = seive(floor(sq(n)))
  if m<=2:
      print(2)
  for i in range(m,n+1):
     if i%2==1 and i!=1:
       for j in primes:
         if i>j and i%j==0:
           break
       else:
         print(i)
  

from sys import stdin,stdout
from time import time
t1=time()
for i in range(1000):
  stdout.write(str(i))
print(t1-time())
t1=time()
for i in range(1000):
  print(i)
print(t1-time())
print("hello")

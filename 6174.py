from time import sleep
for i in range(1001,9999):
  n = i
  while(n!=6174 and len(set(str(n)))>=2):
      val = ''.join(sorted(str(n),reverse = True))
      n = int(val)-int(val[::-1])
      print(n)
  print("\n")

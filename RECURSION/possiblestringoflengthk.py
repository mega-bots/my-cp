#progam to print all possible strings of length k that can be formed from a set of n characters
inp = input("enter the string ").split()
size = len(inp)
k = int(input("enter the k value "))
def comb(ind,arr):
    if (ind==k):
        print("".join(arr))
        return
    for i in inp:
      arr.append(i)
      comb(ind+1,arr)
      arr.pop()
comb(0,[])
def comb1(ind,inp):
    if (ind==size):
        print("".join(inp))
        return
    for i in range(ind,size):
        inp[i],inp[ind]=inp[ind],inp[i]
        comb1(ind+1,inp)
        inp[i],inp[ind]=inp[ind],inp[i]     
comb1(0,inp)




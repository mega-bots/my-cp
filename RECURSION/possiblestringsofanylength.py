#all possible string of any length from a given string
inp = input().split()
another=inp
size =len(inp)
'''
METHOD-1
'''
def comb1(ind,inp,size):
    if (ind==size):
        print("".join(inp),end = " ")
        return
    for i in range(ind,size):
        inp[i],inp[ind]=inp[ind],inp[i]
        comb1(ind+1,inp,size)
        inp[i],inp[ind]=inp[ind],inp[i]     
def possiblestrings(ind,arr):
    if (ind==size):
        return
    for i in range(ind,size):
        arr.append(inp[i])
        comb1(0,arr,len(arr))
        possiblestrings(i+1,arr)
        arr.pop()
#possiblestrings(0,[])

        
'''
METHOD-2
'''
def possible(ind,arr,another):
    for index in range(len(another)):
        arr.append(another[index])
        print("".join(arr),end = " ")
        store = another.pop(index)
        possible(index+1,arr,another)
        #another.insert(index,store)
        another.insert(0,"100")
        arr.pop()
possible(0,[],another)


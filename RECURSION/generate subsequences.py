"""
string  = input()
def generate(ind,subseq,n,string):
    if ind<=n and subseq!="":
        print(subseq)
    for i in range(ind,n):
        generate(i+1,subseq+string[i],n,string)
generate(0,"",len(string),string)


string = list(input())
def generate(ind,n,arr):
    if ind==n:
        print("".join(arr))
    for i in range(ind,n):
        arr[i],arr[ind]=arr[ind],arr[i]
        generate(ind+1,n,arr)
        arr[i],arr[ind]=arr[ind],arr[i]
generate(0,len(string),string)


string = list(input())
def generate(ind,n,subseq,string):
    if ind==n:
        print("".join(subseq))
        return
    generate(ind+1,n,subseq+string[ind],string)
    generate(ind+1,n,subseq,string)
generate(0,len(string),"",string)


number = int(input())
def generate(number,arr):
    if number<=0:
        print("".join(map(str,arr)))
        return 0
    for i in range(1,4):
      generate(number-i,arr+[i])
generate(number,[])


num = int(input("enter a number : " ))
def generate(num,lis):
    if num==0:
        print(lis)
        return 0
    for i in range(1,num+1):
        generate(num-i,lis+[i])
generate(num,[])
print("-"*50)
#program to generate only unique lists
def generate(num,lis,ind):
    if num==0:
        print(lis)
        return 0
    for i in range(1,num+1):
        if i>=ind:
          generate(num-i,lis+[i],i)
generate(num,[],0)
#program to generate subsequences

string = input("enter a string : ")
def generate(ind,n,lis,arr):
    if ind==n:
        print(lis)
        return
    generate(ind+1,n,lis+arr[ind],arr)
    generate(ind+1,n,lis,arr)
generate(0,len(string),"",string)

string = input("enter a string ")
def permute(ind,n,string,arr):
    if ind==n:
        print(arr)
        return
    for i in string:
        permute(ind+1,n,string,arr+i)
permute(0,len(string),string,"")

#program to print combinations
string = input("enter a string: ")
def combine(ind,n,string,arr):
    if ind==n:
        print(arr)
        return 0
    for index,i in enumerate(string):
        val=string.pop(index)
        combine(ind+1,n,string,arr+i)
        string.insert(index,val)
combine(0,len(string),list(string),"")

"""
#generate unique lists by using any number of times
arr = [1,2,1,3]
num = int(input("enter a number "))
def generate(ind,n,num,arr,storage,prev):
    if num<=0:
        if num==0:
          print(storage)
        return 0
    for index,i in enumerate(arr):
        if index>=prev:
            generate(ind+1,n,num-i,arr,storage+[i],index)
arr = list(set(arr))
generate(0,len(arr),num,arr,[],0)

#generate unique lists by using only once

def generate(ind,n,num,arr,storage,prev):
    if (num<=0):
        if(num==0):
            print(storage)
        return 0
    for index,i in enumerate(arr):
      if index>=prev:
        val=arr.pop(index)
        generate(ind+1,n,num-i,arr,storage+[i],index)
        arr.insert(index,val)
#generate(0,len(arr),num,arr,[],0)
    
    








    


    
    
    
    













    

    

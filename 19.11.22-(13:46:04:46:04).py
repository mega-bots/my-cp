memo = set()
c = 0
def solve(ind,string):
    global memo,c
    c+=1
    print(c)
    if ind<=0:
        #print(string)
        memo.add(str(string))
        return
    if ind>=1 :
      while(string[ind]!=0 or string[ind-1]!=0 and str(string) not in memo):
        temp1,temp2 = string[ind],string[ind-1]
        string[ind-1:ind+1]=[string[ind]^string[ind-1]]*2
        if str(string) not in memo:
          solve(ind-1,string)
        string[ind],string[ind-1]=temp1,temp2
        if str(string) not in memo:
          solve(ind-1,string)
        string[ind-1:ind+1]=[string[ind]^string[ind-1]]*2
        
        
string = '11111'
solve(len(string)-1,list(map(int,string)))
print(*memo,sep = '\n')
print(c)

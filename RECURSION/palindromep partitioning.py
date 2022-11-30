#palindrome partitioning
class Solution:
    def __init__(self):
        self.emptyarr = []
    def ispalindrome(self,string):
        return string==string[::-1]
    def solve(self,ind,n,string,storage):
        if ind==n:
            print(storage)
            self.emptyarr.append(storage.copy())
            return self.emptyarr
        
        s = ""
        for i in range(ind,n):
            s+=string[i] 
            if self.ispalindrome(s):
                storage.append(s)
                self.solve(i+1,n,string,storage)
                storage.pop()
            
        
        
    def partition(self, s):
        self.solve(0,len(s),s,[])
        lis = self.emptyarr
        self.emptyarr = []
        return lis

a = Solution()
print(a.partition(input("enter a string: ")))
b = Solution()
print(b.partition(input("enter a string: ")))


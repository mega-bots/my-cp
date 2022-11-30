#daily-challenge-1
"""
https://leetcode.com/problems/minimum-genetic-mutation/
"""
#genetic mutation
class Solution:
    def solve(self,ind,start,end,bank,n):
        if start==end:
            return 1
        maxx=float('inf')
        for i in range(ind,n):
          maxx = float('inf')
          for j in ['A','G','C','T']:
            if start[i]!=j:
              val = start[i]
              if val in bank:
                  start[i]=j
              maxx=max(maxx,self.solve(i+1,start,end,bank,n))
              start[i]=val
        return maxx
          
                  
    def minMutation(self, start, end, bank):
        if bank==[]:
            return -1
        val=self.solve(0,list(start),list(end),list(map(list,bank)),len(bank[0]))
        if val==float('inf'):
            return -1
        else:
            return val
a = Solution()
print("output",a.minMutation("AACCGGTT","AAACGGTA",["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
#"AACCGGTT"
#"AAACGGTA"
#["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]

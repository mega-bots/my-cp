"""
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
"""
#LONGEST-PALINDROME-BY-CONCATENATING
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashtable={}
        for i in words:
            if i not in hashtable:
                hashtable[i]=1
            else:
                hashtable[i]+=1
        tot=0
        
        maxx=0
        check=0
        for i in hashtable:
            val = hashtable[i]
            if (i[::-1] in hashtable and hashtable[i]>1*(i==i[::-1])):
                if i==i[::-1]:
                    tot+=(val//2)*4
                    hashtable[i]=0
                    check = max(check,(val%2)*2)
                    continue
                c = hashtable[i[::-1]]
                tot+=min(val,c)*4
                hashtable[i[::-1]]=0
            elif i==i[::-1]:
                check=2
        return tot+check
           

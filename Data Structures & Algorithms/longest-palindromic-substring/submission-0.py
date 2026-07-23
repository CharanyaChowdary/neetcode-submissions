class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        #result length
        resLength=0
        for i in range(len(s)):
            #ODD Length palindromes
            r=i
            l=i
            while l>=0 and r<len(s) and s[r]==s[l]:
                if r-l+1>resLength:
                    res=s[l:r+1]
                    resLength=r-l+1
                l-=1
                r+=1

            #EVEN Length palindromes
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                if r-l+1>resLength:
                    res=s[l:r+1]
                    resLength=r-l+1
                l-=1
                r+=1

        return res
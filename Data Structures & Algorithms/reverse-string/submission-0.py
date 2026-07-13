class Solution:
    def reverseString(self, s: List[str]) -> None:
        r=0
        l=len(s)-1
        while r<l:
            s[r],s[l]=s[l],s[r]
            r=r+1
            l=l-1
        
        
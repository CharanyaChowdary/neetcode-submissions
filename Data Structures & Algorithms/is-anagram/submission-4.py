class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)!=len(t):
            return False
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in t:
            if i not in freq:
                return False
            freq[i]-=1
            if freq[i]<0:
                return False
        return True
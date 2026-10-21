class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for i in range(len(s)):
            freq[s[i]]=1+freq.get(s[i],0)
        for j in range(len(t)):
            if t[j] not in freq:
                return False
            freq[t[j]]-=1
            if freq[t[j]]<0:
                return False
        return True

        
        
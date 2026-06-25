class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        def isAnagram(a,s):
            if len(a)!=len(s):
                return False
            counter={}
            for i in a:
                counter[i]=counter.get(i,0)+1
            for i in s:
                if i not in counter:
                    return False
                counter[i]-=1
                if counter[i]<0:
                    return False
            return True
        visited=set()
        for i in range(len(strs)):
            if i in visited:
                continue
           
            temp=[strs[i]]
            visited.add(i)
            for j in range(i+1,len(strs)):
                if j not in visited and isAnagram(strs[i],strs[j]):
                    temp.append(strs[j])
                    visited.add(j)
            output.append(temp)
        return output

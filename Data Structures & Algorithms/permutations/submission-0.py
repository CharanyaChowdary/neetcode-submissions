class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking solution for this
        res=[]
        used=[False]*len(nums)
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i]=False



        backtrack([])
        return res
        
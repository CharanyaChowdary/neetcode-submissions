class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=set(nums)
        l1=len(nums)
        l2=len(n)
        return l1!=l2
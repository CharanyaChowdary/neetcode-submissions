class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums)-1)
        n=len(nums)
        #as it is circular including first and last should not be done
        #to avoid that we use two dp arrays
        #dp1 array for 0 t0 n-2 (last house is excluded) 
        dp1[0]=nums[0]
        dp1[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i])
        #dp2 array for 1 to n-1 (first is excluded now)
        dp2[0]=nums[1]
        dp2[1]=max(nums[1],nums[2])
        for i in range(2,n-1):
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i+1])
        return max(dp1[-1],dp2[-1])
        
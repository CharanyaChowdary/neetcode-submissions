class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        output = [0] * len(nums)

        pref[0] = nums[0]

        for i in range(1, len(nums)):
            pref[i] = nums[i] * pref[i-1]

        suff[-1] = nums[-1]

        for j in range(len(nums)-2, -1, -1):
            suff[j] = nums[j] * suff[j+1]

        for i in range(len(nums)):
            if i == 0:
                output[i] = suff[i+1]

            elif i == len(nums)-1:
                output[i] = pref[i-1]

            else:
                output[i] = suff[i+1] * pref[i-1]

        return output
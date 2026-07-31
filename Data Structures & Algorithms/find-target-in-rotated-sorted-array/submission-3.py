class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        while right>=left:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            #if left half is sorted
            if nums[mid]>=nums[left]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            #right half is sorted
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
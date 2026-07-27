class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):

            # Check duplicate
            if nums[right] in window:
                return True

            # Add current element
            window.add(nums[right])

            # Keep only the last k elements
            if right - left >= k:
                window.remove(nums[left])
                left += 1

        return False
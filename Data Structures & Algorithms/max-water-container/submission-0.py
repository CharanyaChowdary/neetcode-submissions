class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        left=0
        right=len(heights)-1
        while right>left:
            area=(right-left)*min(heights[right],heights[left])
            maxArea=max(area,maxArea)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return maxArea
        
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search_row(low,high,row):
            while low<=high:
                mid=low+(high-low)//2
                if row[mid]==target:
                    return True
                elif row[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return False
        m=len(matrix)
        n=len(matrix[0])
        if m==0:
            return False
        if (m==1 and n==1):
            if matrix[0][0]==target:
                return True
            return False

        left=0
        right=m-1
        while left<=right:
            mid=left+(right-left)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<=target:
                if matrix[mid][n-1]>=target:
                    return binary_search_row(0,n-1,matrix[mid])
                else:
                    left=mid+1
            elif matrix[mid][0]>target:
                right=mid-1
        return False
            
        

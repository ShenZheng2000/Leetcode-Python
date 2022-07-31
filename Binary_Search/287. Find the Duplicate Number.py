class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Purpose: find the duplicate num in array
        # Method: Binary Search
        # Intuition: iteratively count numbers small than mid, if miss sth, check right side, if duplicates, check left side
        
        # init
        left = 0
        right = len(nums) - 1
        
        # find 
        while left < right:
            
            mid = (left + right) // 2

            count = sum(i <= mid for i in nums)
            
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        
        # return
        return right

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Purpose: find peak elements' index
        # Method: Binary Search
        # Intuition: Increase -> check right; else -> check left
        
        # init
        left = 0
        right = len(nums) - 1
        
        # find 
        while left < right:
            
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            
            else:
                right = mid
        
        # return
        return left

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Purpose: find min int in rotated array
        # Method: Binary Search
        # Intuition: mid < right -> check left; else, check right
        
        # init
        left = 0
        right = len(nums) - 1
        
        # find 
        while left < right:
            
            mid = (left + right) // 2
            
            if nums[mid] <= nums[right]:
                right = mid
                
            else:
                left = mid + 1
        
        # return
        return nums[left]

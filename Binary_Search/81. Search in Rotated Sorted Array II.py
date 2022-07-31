class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Purpose: find element's ind in rotated array (possibly duplicates; return T/F)
        # Method: Binary Search 
        # Intuition: split into mid-in-left and mid-in-right, then check target
        
        # init
        left = 0
        right = len(nums) - 1
        
        # find 
        while left <= right:
            
            mid = (left + right) // 2
            
            while left < mid and nums[left] == nums[mid]:
                left += 1
            
            if target == nums[mid]:
                return True
            
            elif nums[left] <= nums[mid]:
                
                if nums[left] <= target <= nums[mid]:
                    right = mid
                    
                else:
                    left = mid + 1
            
            else:
                
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid
        
        # return
        return False

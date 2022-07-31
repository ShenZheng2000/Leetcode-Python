class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Purpose: search element's ind in a rotated array
        # Method: binary search 
        # Intuition: split into mid-in-left and mid-in-right case, then check target
        
        # init
        left = 0
        right = len(nums) - 1
        
        # find 
        while left <= right:
            
            # cal mid
            mid = (left + right) // 2
            
            # match
            if target == nums[mid]:
                return mid
            
            # mid-in-left
            elif nums[left] <= nums[mid]:
                
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                    
                else:
                    left = mid + 1
            
            # mid-in-right
            else:
                
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid - 1
        
        # return
        return -1

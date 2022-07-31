class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Purpose: find index that splits increasing and decreasing trend
        # Method: Binary Search
        # Intuition: Increase -> check right; else -> check left
        
        # init
        left = 0
        right = len(arr) - 1
        
        # find 
        while left < right:
            
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
                
            else:
                right = mid
        
        # return 
        return left

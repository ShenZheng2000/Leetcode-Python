class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Purpose: find the k closest elements for an int x in array
        # Method: Binary Search
        # Intuition: search left if better or equal, search right if better
        
        # cc1: left OOB
        if x <= arr[0]:
            return arr[:k]
        
        # cc2: right OOB
        if x >= arr[-1]:
            return arr[-k:]
        
        # init
        left = 0
        right = len(arr) - k
        
        # find 
        while left < right:
            
            mid = (left + right) // 2
            
            if abs(x - arr[mid]) <= abs(x - arr[mid + k]):
                right = mid
                
            else:
                left = mid + 1
        
        # return
        return arr[left:left+k]
        

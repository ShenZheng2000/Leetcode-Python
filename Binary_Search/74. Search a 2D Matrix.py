class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Purpose: check if a value exist on a 2D matrix
        # Method: Binary Search
        # Intuition: find specific row, then specific element in that row
        
        row = self.find_row(matrix, target)
        if row is None: return False
        return self.find_ele(matrix, target, row)
        
    
    def find_row(self, matrix, target):
        top = 0
        bot = len(matrix) - 1
        
        while top <= bot:
            
            row = (top + bot) // 2
            
            if target < matrix[row][0]:
                bot = row - 1
            
            elif target > matrix[row][-1]:
                top = row + 1
            
            else:
                return row
            
    
    def find_ele(self, matrix, target, row):
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if target < matrix[row][mid]:
                right = mid - 1
                
            elif target > matrix[row][mid]:
                left = mid + 1
            
            else:
                return True
            
        return False
                

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Purpose: search an element in a 2D matrix
        # Method: Two Pointers
        # Intuition: start at upper right, if small, go left, if large, go right
        
        # init
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        row = 0
        col = COLS - 1
        
        # find 
        while row < ROWS and col >= 0:
            
            if target == matrix[row][col]:
                return True
            
            elif target < matrix[row][col]:
                col -= 1
            
            else:
                row += 1
                
        
        # return
        return False

################## Following is the heap solution ######################
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Purpose: find kth smallest element in a sorted matrix
        # Method: Heap
        # Intuition: traverse the matrix, mark neg val, push till k, replace with smaller vals
        # Example 1: 
        #           matrix = [[1,2],[1,3]], k = 2
        #           heap = [] -push-> [-1] -push-> [-2, -1] -pushpop-> [-1, -1]
        #           res = 1
        # Example 2: 
        #           matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
        #           heap = [] -push-> [-1] -push-> [-5, -1] -push-> ... [-13, -13, -12, -10, -9, -5, -11, -1]
        #           res = 13
        
        # init
        ROWS = len(matrix)
        COLS = len(matrix[0])
        heap = []
        
        # traverse the matrix
        for row in range(ROWS):
            for col in range(COLS):

                # mark neg val
                neg_val = -matrix[row][col]

                # push till k
                if len(heap) < k:
                    heapq.heappush(heap, neg_val)

                # replace with smaller vals
                elif neg_val > heap[0]:
                    heapq.heappushpop(heap, neg_val)
                
        # return
        return -heap[0]
    
    
    
    
#################### Following is the binary search solution ############################
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Purpose: find kth smallest element in a sorted (a. for r & c) matrix
        # Method: Binary Search
        # Intuition: count elements that is <= mid. if count < k, check right; else, check left
        
        # init
        left = matrix[0][0]
        right = matrix[-1][-1]
        
        # find 
        while left < right:
            
            mid = (left + right) // 2
            
            count = self.find_count(matrix, mid)
            
            if count < k:
                left = mid + 1
                
            else:
                right = mid
        
        # return
        return left
    
    
    def find_count(self, matrix, mid):
        count = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] <= mid:
                    count += 1
        
        return count

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

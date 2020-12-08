Given a positive integer n, generate an n x n matrix filled 
with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
 
Constraints:
1 <= n <= 20


# My Solution
# O(n^2) Time and O(1) Space
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        row_start, column_start = 0, 0
        row_end, column_end = n-1, n-1
        
        value = 1
        
        result = [[0 for j in range(n)] for i in range(n)]
        
        while row_start <= row_end and column_start <= column_end:
            
            for i in range(column_start, column_end+1):
                result[row_start][i] = value
                value += 1
                
            row_start += 1
            
            for i in range(row_start, row_end+1):
                result[i][column_end] = value
                value += 1
            
            column_end -= 1
            
            if row_start <= row_end:
                
                for i in range(column_end, column_start-1, -1):
                    result[row_end][i] = value
                    value += 1
            row_end -= 1
            
            if column_start <= column_end:
                
                for i in range(row_end, row_start-1, -1):
                    result[i][column_start] = value
                    value += 1
            
            column_start += 1
            
        
        return result
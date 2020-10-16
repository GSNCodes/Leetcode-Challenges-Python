Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:
Input: matrix = [], target = 0
Output: false
 

Constraints:
m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104



# My Solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not any(matrix):
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        i=0
        while i<m and matrix[i][n-1] <= target:
            if matrix[i][n-1] == target:
                return True
            i += 1
        
        if i == m:
            return False
            
        for j in range(n):
            if matrix[i][j] == target:
                return True
        
        return False

# Another Approach - Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not any(matrix):
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m*n - 1
        
        while left <= right:
            mid = left + (right-left)//2
            
            mid_element = matrix[mid//n][mid%n]
            
            if mid_element == target:
                return True
            
            elif mid_element < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return False
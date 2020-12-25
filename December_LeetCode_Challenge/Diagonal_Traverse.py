Given a matrix of M x N elements (M rows, N columns), 
return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.

# O(m*n) Time and O(1) Space
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        row = 0
        col = 0
        m, n = len(matrix), len(matrix[0])
        
        isUp = True
        result = []
        
        while row<m and col<n:
            
            if isUp:
                
                while row>0 and col<n-1:
                    result.append(matrix[row][col])
                    row -= 1
                    col += 1
                
                result.append(matrix[row][col])
                
                if col == n-1:
                    row += 1
                else:
                    col += 1
            
            else:
                
                while col>0 and row<m-1:
                    result.append(matrix[row][col])
                    row += 1
                    col -= 1
                
                result.append(matrix[row][col])
                
                if row == m-1:
                    col += 1
                else:
                    row += 1
                    
            isUp = not isUp            
            
                    
        return result

# An easy to understand solution
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d={}
        #loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                #if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                #If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
        # we're done with the pass, let's build our answer array
        ans= []
        #look at the diagonal and each diagonal's elements
        for entry in d.items():
            #each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
            #snake time, look at the diagonal level
            if entry[0] % 2 == 0:
                #Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans

# Key Concept
1. Diagonals are defined by the sum of indicies in a 2 dimensional array
2. The snake phenomena can be achieved by reversing every other diagonal level, therefore check if divisible by 2
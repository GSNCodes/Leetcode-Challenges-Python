In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the ith domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, 
or all the values in B are the same.
If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, 
as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:
2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6


# O(n) Time and O(1) Space
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        min_swaps = min(
            self.swapCount(A[0], A, B),
            self.swapCount(B[0], A, B),
            self.swapCount(A[0], B, A),
            self.swapCount(B[0], B, A)
        )
        
        return -1 if min_swaps == float('inf') else min_swaps
    
    
    def swapCount(self, target, arr1, arr2):
        numSwaps = 0
        
        for i in range(len(arr1)):
            
            if arr1[i] != target and arr2[i] != target:
                return float('inf')
            
            elif arr1[i] != target:
                numSwaps += 1
                
        return numSwaps
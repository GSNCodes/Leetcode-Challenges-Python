Let-s call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?




# My Solution
# O(n) Time and O(1) Space
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        
        n = len(A)
        max_len = 0
        for i in range(1,n-1):
            
            if A[i] > A[i-1] and A[i] > A[i+1]:
                left  = i
                right = i
                while left-1 >= 0 and A[left-1] < A[left]:
                    left -= 1
                    
                while right+1 < n and A[right+1] < A[right]:
                    right += 1
                    
                if max_len < right - left + 1 and right-left+1 >= 3:
                    max_len = right - left + 1
                    
        return max_len
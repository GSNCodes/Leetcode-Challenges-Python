Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104



# My Solution
# O(n) Time and O(1) Space
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        increasing_flag, decreasing_flag = False, False
        
        for i in range(len(arr)-1):
            
            if arr[i] == arr[i+1]:
                return False
            
            if arr[i] < arr[i+1]:
                
                if decreasing_flag:
                    return False
                
                increasing_flag = True
                
            if arr[i] > arr[i+1]:
                
                decreasing_flag = True
        
        if decreasing_flag and increasing_flag:
            return True

#Alternate Solution
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1





Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  
Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""
 
Note:
A.length == 4
0 <= A[i] <= 9

# O(1) Time and O(1) Space
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        largest_time = -1
        for h1, h2, m1, m2 in permutations(A):
            
            hours   = h1*10 + h2
            minutes = m1*10 + m2
            
            if 0<=hours<24 and 0<=minutes<60:
                largest_time = max(largest_time, hours*60 + minutes)
                
        if largest_time == -1:
            return ""
        
        return f"{largest_time//60:02}:{largest_time%60:02}"
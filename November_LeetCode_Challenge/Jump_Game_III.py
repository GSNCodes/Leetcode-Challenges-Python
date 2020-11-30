Given an array of non-negative integers arr, 
you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], 
check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 
Constraints:
1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length




# My Solution
# O(n) Time and O(n) Space
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        stack = []
        
        seen = [0 for i in range(len(arr))]
        
        stack.append(start)
        
        while stack:
            
            m = stack.pop()
            l = m - arr[m]
            r = m + arr[m]
            
            if l>=0 and l<len(arr) and seen[l] == 0:
                stack.append(l)
                seen[l] = 1
                
                if arr[l] == 0:
                    return True
            
            if r>=0 and r<len(arr) and seen[r] == 0:
                stack.append(r)
                seen[r] = 1
                
                if arr[r] == 0:
                    return True
                
        return False

# DFS - # O(n) Time and O(n) Space
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])

        return False
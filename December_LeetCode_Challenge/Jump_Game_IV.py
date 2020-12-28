Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. 
Note that index 9 is the last index of the array.

Example 2:
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don-t need to jump.

Example 3:
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:
Input: arr = [6,1,9]
Output: 2

Example 5:
Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 

Constraints:
1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8


# O(n) Time and O(n) Space
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        if n == 1:
            return 0
        
        mappings = defaultdict(list)
        jumps = 0
        
        for i, num in enumerate(arr):
            mappings[num].append(i)
            
        
        queue = [0]
        
        while len(queue) > 0:
            jumps += 1
            
            size = len(queue)
            
            for i in range(size):
                
                j = queue.pop(0)
                
                if j-1 >= 0 and arr[j-1] in mappings:
                    
                    queue.append(j-1)
                    
                if j+1 < n and arr[j+1] in mappings:
                    
                    if j+1 == n-1:
                        return jumps
                    
                    queue.append(j+1)
                
                if arr[j] in mappings:
                    
                    for k in mappings[arr[j]]:
                        
                        if k != j:
                            
                            if k == n-1:
                                return jumps
                            
                            queue.append(k)
                
                if arr[j] in mappings:
                    del mappings[arr[j]]
                
            
            
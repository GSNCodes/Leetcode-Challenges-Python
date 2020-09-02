Given an array of integers, find out whether there are two distinct indices i and j 
in the array such that the absolute difference between nums[i] and nums[j] 
is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

Hint #1  
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.

Hint #2  
Use already existing state to evaluate next state - 
Like, a set of k sorted numbers are only needed to be tracked. 
When we are processing the next number in array, 
then we can utilize the existing sorted state and it is not necessary 
to sort next overlapping set of k numbers again.


#O(n*k) Time and O(1) Space
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        size = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            return False
        
        for i, cur_val in enumerate(nums):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(cur_val - nums[j]) <= t:
                    return True
                    
        return False


#O(nlogk) Time and O(k) Space
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        bst_list = SortedList()
        for i in range(len(nums)):
            if i > k: 
                bst_list.remove(nums[i-k-1])   
            pos1 = bisect_left(bst_list, nums[i] - t)
            pos2 = bisect_right(bst_list, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(bst_list): 
                return True
            
            bst_list.add(nums[i])
        
        return False
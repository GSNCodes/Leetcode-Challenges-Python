Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

# O(n) Time and O(1) Space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 0:
            return 1
        
        contains_one = False
        
        for i,num in enumerate(nums):
            if num == 1:
                contains_one = True
                
            if num<=0 or num>n:
                nums[i] = 1
                
        
        if not contains_one:
            return 1
        
        
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        for i,num in enumerate(nums):
            if num > 0:
                return i+1
            
        return n+1
                
                
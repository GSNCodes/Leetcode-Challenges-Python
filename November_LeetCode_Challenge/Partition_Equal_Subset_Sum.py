Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

# O(m*n) Time and O(m*n) Space where n is the number of elements and m is the total value
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.states = {}
        total = sum(nums)
        
        if total%2 != 0:
            return False
        
        return self.helper(nums, 0, 0, total)
    
    def helper(self, nums, index, sum_val, total):
        
        current = str(index) + str(sum_val)
        
        if current in self.states:
            return self.states[current]
        
        if sum_val*2 == total:
            return True
        
        if sum_val > total / 2 or index >= len(nums):
            return False
        
        partition_found = self.helper(nums, index+1, sum_val, total) or self.helper(nums, index+1, sum_val + nums[index], total)
        
        self.states[current] = partition_found
        
        return partition_found
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# O(n) Time and O(1) Space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for num in nums[1:]:
            
            temp_max = current_max
            
            current_max = max(num, current_max*num, current_min*num)
            current_min = min(num, temp_max*num, current_min*num)
            
            if current_max > max_product:
                max_product = current_max
                
        
        return max_product
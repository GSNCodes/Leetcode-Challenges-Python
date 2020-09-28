Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.


# My Solution
# O(n) Time and O(1) Space
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        
        product = 1
        result = 0
        left, right = 0, 0
        
        while right<len(nums):
            
            product *= nums[right]
            
            while product >= k:
                product /= nums[left]
                left += 1
                
            result += right-left + 1
            
            right += 1
            
        return result 
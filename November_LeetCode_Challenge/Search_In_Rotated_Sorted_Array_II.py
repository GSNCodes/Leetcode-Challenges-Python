Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?


# O(n) Time and O(n) Space
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        low = 0
        high = len(nums)
        while low<high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] and nums[high-1] == nums[mid]:
                low +=1
                high -=1
                continue
            if nums[low]<=nums[mid]:
                if target >=nums[low] and target <nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if target<=nums[high-1] and target>nums[mid]:
                    low = mid+1
                else:
                    high = mid
        return False 
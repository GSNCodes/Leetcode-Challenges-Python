You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x 
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Example 3:
Input: nums = []
Output: []

Example 4:
Input: nums = [-1]
Output: ["-1"]

Example 5:
Input: nums = [0]
Output: ["0"]
 
Constraints:
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.




# My Solution
# O(n) Time and O(1) Space
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if nums is None:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        if len(nums) == 2:
            if nums[0]+1 == nums[1]:
                return [str(nums[0])+'->'+str(nums[1])]
            else:
                return [str(nums[0]), str(nums[1])]
        
        
        start, end = 0, 0
        result = []
        
        for i in range(len(nums)):
            
            if i<len(nums)-1 and nums[i]+1 == nums[i+1]:
                end += 1
                
            else:
                
                if start == end:
                    result.append(str(nums[start]))
                    
                else:
                    result.append(str(nums[start])+'->'+str(nums[end]))
                    
                
                start = end + 1
                end += 1
                   
                
                
        return result
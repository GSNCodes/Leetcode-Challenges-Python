Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

# My Solution
# O(nlogn) Time and O(n)/O(1) Space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squared = list(map(lambda x: x*x, nums))
        squared.sort()
        
        
        return squared



# Alternate Solution without using the in-built sort function
# O(n) Time and O(n)/O(1) Space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        positive_ptr = 0
        
        while positive_ptr < n and nums[positive_ptr] < 0:
            positive_ptr += 1
            
        
        negative_ptr = positive_ptr - 1
        
        result = []
        
        index = 0
        
        while negative_ptr >=0 and positive_ptr < n:
            
            if nums[positive_ptr]*nums[positive_ptr] <= nums[negative_ptr]*nums[negative_ptr]:
                
                result.append(nums[positive_ptr]*nums[positive_ptr])
                positive_ptr += 1
                
            else:
                result.append(nums[negative_ptr]*nums[negative_ptr])
                negative_ptr -= 1
                
            index += 1
            
        while negative_ptr >=0 :
            result.append(nums[negative_ptr]*nums[negative_ptr])
            negative_ptr -= 1
            
        while positive_ptr < n:
            result.append(nums[positive_ptr]*nums[positive_ptr])
            positive_ptr += 1
                
        return result
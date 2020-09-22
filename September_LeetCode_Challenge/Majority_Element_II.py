Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

Hint #1  
How many majority elements could it possibly have?


# O(n) Time and O(1) Space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)//3
        
        candidate_1 = None
        candidate_2 = None
        vote_1 = 0
        vote_2 = 0
        
        
        for num in nums:
            
            if candidate_1 == num:
                vote_1 += 1
                
            elif candidate_2 == num:
                vote_2 += 1
                
            elif vote_1 == 0:
                candidate_1 = num
                vote_1 += 1
                
            elif vote_2 == 0:
                candidate_2 = num
                vote_2 += 1
                
            else:
                vote_1 -= 1
                vote_2 -= 1
        
        
        
        result = []
        for c in [candidate_1, candidate_2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result
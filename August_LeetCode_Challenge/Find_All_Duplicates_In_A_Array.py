Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]


# O(n) Time and O(1) Space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        output = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] = -nums[abs(num)-1]
                
            else:
                output.append(abs(num))
                
        return output

# O(n) Time and O(n) Space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        output = []
        mappings = Counter(nums)
        for element in mappings.items():
            if element[1]>1:
                output.append(element[0])
        
        return output
                
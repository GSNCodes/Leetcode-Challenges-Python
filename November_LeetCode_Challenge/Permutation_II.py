Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# A Solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        n = len(nums)
        result = []
        
        def dfs(nums, l):
            if l == n-1:
                result.append(list(nums))
                return 
            for i in range(l, n):
                if i > l and nums[i] == nums[l]: 
                    continue
                nums[l], nums[i] = nums[i], nums[l] 
                
                dfs(list(nums), l+1)
        
        nums.sort()
        dfs(nums, 0)
        return result
            

  
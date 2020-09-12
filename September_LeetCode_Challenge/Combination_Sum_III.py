Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def helper(start, target, res):
            
            if target==0 and len(res) == k:
                
                result.append(res)
                
                return
            
            if target<0 or len(res) == k:
                return
            
            for i in range(start,10):
                if i not in res:
                    helper(i,target-i,res+[i])
        
        
        
        
        result = []
        
        helper(1, n, [])
        
        return result
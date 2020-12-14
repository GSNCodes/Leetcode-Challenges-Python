Given n balloons, indexed from 0 to n-1. Each balloon is painted 
with a number on it represented by array nums. You are asked to burst all the balloons. 
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left 
and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


# O(n^3) Time and O(n^2) Space
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n==0:
            return 0
        
        
        dp = [[-1 for i in range(n)] for j in range(n)]
        
        for l in range(n):
            
            i = 0
            
            while i+l < n:
                
                r = i+l
                
                for k in range(i, r+1):
                    
                    left_num = 1 if i==0 else nums[i-1]
                    right_num = 1 if r==n-1 else nums[r+1]
                    
                    dp_left = 0 if k==i else dp[i][k-1]
                    dp_right = 0 if k==r else dp[k+1][r]
                    
                    
                    dp[i][r] = max(dp[i][r], left_num*nums[k]*right_num + dp_left + dp_right)
                
                i += 1
                
        
        return dp[0][n-1]
                
            
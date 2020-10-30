Given an integer array nums, return the number of longest increasing subsequences.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 
Constraints:
0 <= nums.length <= 2000
-106 <= nums[i] <= 106



# O(n^2) Time and O(n) Space
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp  = [0 for i in range(n)]
        cnt = [0 for i in range(n)]
        
        maxlen, result = 0, 0
        
        for i in range(n):
            dp[i], cnt[i] = 1, 1
            
            for j in range(i):
                
                if nums[j] < nums[i]:
                    
                    if dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                    
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                
            if maxlen == dp[i]:
                result += cnt[i]
            
            if maxlen < dp[i]:
                maxlen = dp[i]
                result = cnt[i]
                
        
        return result 
                        
            
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 
Example 1:
Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. 
We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:
Input: s = "1"
Output: 1
 
Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).




# O(n) Time and O(n) Space
class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 0 if s[0]=='0' else 1
        
        for i in range(2, len(s)+1):
            
            one_digit = s[i-1:i]
            two_digits = s[i-2:i]
            
            if int(one_digit) >= 1:
                dp[i] += dp[i-1]
            
            if 10 <= int(two_digits) <= 26:
                dp[i] += dp[i-2]
            
        
        return dp[-1]
Given a string s and an integer k, return the length of the longest substring of s 
such that the frequency of each character in this substring is less than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105

# O(n^2) Time and O(1) Space
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        n = len(s)
        
        if n==0 or n<k:
            return 0
        
        if k<=1:
            return n
        
        count = Counter(s)
        
        l = 0
        
        while l < n and count[s[l]] >= k:
            l += 1
            
        if l >= n-1:
            return l
        
        ls1 = self.longestSubstring(s[0:l], k)
        
        while l < n and count[s[l]] < k:
            l += 1
            
        ls2 = self.longestSubstring(s[l:], k) if l<n else 0
        
        return max(ls1, ls2)
        
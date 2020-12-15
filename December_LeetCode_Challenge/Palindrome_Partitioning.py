Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.



# My Solution
# O(n * 2^n) Time and O(n) Space
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.result = []
        
        if len(s) == 0:
            return self.result
        
        self.helper([], s, 0)
        
        return self.result
        
    def helper(self, current, s, low):
        
        if low == len(s):
            self.result.append(current[:])
            return 
        
        for high in range(low, len(s)):
            
            if self.isPalindrome(s, low, high):
                current.append(s[low:high+1])
                self.helper(current, s, high+1)
                current.pop()
                
    def isPalindrome(self, s, low, high):
        
        while low<=high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
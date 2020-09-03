Given a non-empty string check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only 
and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It-s the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It-s the substring "abc" four times. (And the substring "abcabc" twice.)

#My Solution
# O(n*sqrt(n)) Time and O(n) Space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if len(s)<=1:
        #     return False
        for i in range(len(s)//2,0,-1):
            
            if len(s)%i == 0:
                
                num_blocks = len(s)//i
                
                temp_str = ''
                
                for j in range(num_blocks):
                    temp_str += ''.join(s[:i])
                
                if temp_str == s:
                    return True
                
            
        return False

#Concise Solution
#O(n) Time and O(n) Space          
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1: -1]
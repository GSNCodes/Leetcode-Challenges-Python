Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: 
ttps://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
 
Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


# O(n) Time and O(1) Space
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = [0 for i in range(26)]
        
        for c in s:
            count [ord(c)-ord('a')] += 1
            
        used = [False for i in range(26)]
        result = []
        
        for c in s:
            count[ord(c)-ord('a')] -= 1
            
            if used[ord(c)-ord('a')]:
                continue
                
            while len(result)>0 and ord(c) < ord(result[-1]) and count[ord(result[-1]) - ord('a')] > 0:
                used[ord(result[-1])-ord('a')] = False
                result.pop()
            
            result.append(c)
            used[ord(result[-1])-ord('a')] = True
        
        return ''.join(result)
            
Given a string s, the power of the string is the maximum length of a non-empty 
substring that contains only one unique character.

Return the power of the string.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "triplepillooooow"
Output: 5

Example 4:
Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:
Input: s = "tourist"
Output: 1

# My Solution
# O(n) Time and O(n) Space
class Solution:
    def maxPower(self, s: str) -> int:
        power = [0 for i in range(len(s))]
        power[0] = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                power[i] = power[i-1] + 1
                
            else:
                power[i] = 1
                
        return max(power)
            


# O(n) Time and O(1) Space
class Solution:
    def maxPower(self, s: str) -> int:
        curr=''
        count=0
        mx=0
        for i in s:
            if i == curr:
                count+=1
            else:
                curr = i
                if count > mx:
                    mx = count
                count=0
                
        if count > mx:
                mx = count
        return mx + 1
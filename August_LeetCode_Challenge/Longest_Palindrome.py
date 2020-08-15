Given a string which consists of lowercase or uppercase letters, find the length of the 
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        final_length = 0
        count = 0
        mappings = Counter(s)
        
        for key in mappings:
            final_length += mappings[key]//2 * 2
            count += mappings[key]%2
           
                
        if count > 0:
            return final_length + 1
        
        return final_length
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        
        string = []
        for char in s:
            if char.isalnum() and char!= ' ':
                string.append(char.lower())
        
        print(string)
        return string == string[::-1]



        
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(re.findall("[a-zA-Z0-9]", s)).lower()
        return s == s[::-1]
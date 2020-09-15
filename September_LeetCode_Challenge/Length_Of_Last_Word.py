Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

#My Solution 
#O(n) Time and O(m) Space where m is the number of words and n is the number of characters
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        word_list = s.split()
        
        if len(word_list)==0:
            return 0
        
        return len(word_list[-1])

# Shorter solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.split():
            return len(s.split()[-1])
        return 0

# Solution without using in-built functions
# O(n) Time and O(1) space where m is the number of characters
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        
        if len(s)==1 and s[0]!=' ':
            return 1
        

        last_space_index = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] != ' ':
                break
            
            else:
                last_space_index += 1
        
        end_word_length = 0
        for i in range(len(s)-last_space_index-1, -1, -1):
            if s[i] != ' ':
                end_word_length += 1
                
            else:
                break
                
        return end_word_length
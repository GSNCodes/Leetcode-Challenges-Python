All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated 
sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 
Constraints:
0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.

# My Solution
# O(n) Time and O(n) Space
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        
        result = []
        mappings = defaultdict(int)
        
        i=0
        
        while i+10 <= len(s):
            
            substring = s[i:i+10]
            
            mappings[substring] += 1
            
            if mappings[substring] == 2:
                result.append(substring)
                
            i += 1
            
        return result
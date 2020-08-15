Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701
 

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".


class MySolution:
    def titleToNumber(self, s: str) -> int:
        column_number = 0
        for i,char in enumerate(s):
            column_number += (ord(char)-ord('A') + 1)*(26**(len(s)-i-1)) 
        
        return column_number


class Solution:
    def titleToNumber(self, s: str) -> int:
        ord_A = ord('A')
        power = 1
        res = 0
        for l in reversed(s):
            res += (ord(l) - ord_A + 1) * power
            power *= 26
            
        return res
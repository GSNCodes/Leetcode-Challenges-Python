Given a positive integer n, find the smallest integer which has 
exactly the same digits existing in the integer n and is greater in value than n. 
If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, 
if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1
 
Constraints:
1 <= n <= 231 - 1


# O(n) Time and O(1) Space
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        digit_count = [0 for i in range(10)]
        
        current_digit = -1
        prev_digit = -1
        
        while n > 0:
            
            current_digit = n % 10
            n = n//10
            digit_count[current_digit] += 1
            
            if prev_digit > current_digit:
                
                digit = current_digit + 1
                
                while digit_count[digit] == 0:
                    digit += 1
                
                digit_count[digit] -= 1
                
                n = n*10 + digit
                
                for i in range(10):
                    while digit_count[i] > 0:
                        n = n*10 + i
                        digit_count[i] -= 1
                
                return n if n<(2**31)-1 else -1
            
            prev_digit = current_digit
            
        return -1
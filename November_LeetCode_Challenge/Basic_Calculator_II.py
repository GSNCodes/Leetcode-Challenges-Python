Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces. 
The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.



# O(n) Time and O(n) Space
class Solution:
    def calculate(self, s: str) -> int:
        
        stack, current_number, operator = [], 0, "+"
        operators = {"+", "-", "*", "/"}
        
        for indx in range(len(s)):
            char = s[indx]
            
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if char in operators or indx == len(s) - 1:
                if operator == "+":
                    stack.append(current_number)
                    
                elif operator == "-":
                    stack.append(-current_number)
                    
                elif operator == "*":
                    stack[-1] *= current_number
                
                elif operator == "/":
                    stack[-1] = int(stack[-1] / current_number)
                    
                current_number = 0
                operator = char
            
        return sum(stack)
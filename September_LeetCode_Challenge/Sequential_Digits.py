An integer has sequential digits if and only if each digit in the number 
is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
10 <= low <= high <= 10^9

Hint #1  
Generate all numbers with sequential digits and check if they are in the given range.

Hint #2  
Fix the starting digit then do a recursion that tries to append all valid digits.

# My Solution
# O(nlogn) Time and O(n) Space where n is the number of sequential digits in the given range
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        result = []
        
        for digit in range(1, 10):
            
            number = digit
            next_digit = digit
            while number <= high and next_digit<10:
                
                if number >= low:
                    result.append(number)
                
                next_digit += 1
                number = (number*10) + next_digit
                
                
        return sorted(result)
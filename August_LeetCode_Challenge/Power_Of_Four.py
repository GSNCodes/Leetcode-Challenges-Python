Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?



import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        if num<=0:
            return False
        
        
        x = log(num,4)
        
        return x==int(x)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        while num%4 == 0:
            num /= 4
        return True if num==1 else False

class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num


class Solution:
    def isPowerOfFour(self, num):
        if num<= 0:
            return False
        z = bin(num)[::-1]
        if z.count('1') > 1:
            return False
        p = z.index('1')
        return p % 2 == 0
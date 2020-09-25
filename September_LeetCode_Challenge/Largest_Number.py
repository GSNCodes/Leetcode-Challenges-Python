Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.


# O(nlogn) Time and O(n) Space
class Compare(str):
    def __lt__(x, y):
        return x+y > y+x
    

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ""
        
        s_list = list(map(lambda x: str(x), nums))
        s_list.sort(key=Compare)
        # print(s_list)
        result = ''.join(s_list)
        
        
        return '0' if result[0] == '0' else result
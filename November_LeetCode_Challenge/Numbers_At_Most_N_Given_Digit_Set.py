Given an array of digits, you can write numbers using each digits[i] as many times as we want.  
 example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.


Example 1:
Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:
Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.

Example 3:
Input: digits = ["7"], n = 8
Output: 1
 
Constraints:
1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109



# A Good Solution
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nstr = str(n)
        n1st = nstr[0]        
        # base case
        if n < 10: return sum(d<=n1st for d in digits)

        # case 1
        case1 = 0
        for i in reversed(range(1,len(nstr))): case1 += len(digits)**i
        # case 2
        case2 = sum(d<n1st for d in digits) * (len(digits) ** (len(nstr)-1))
        # case 3
        case3 = 0
        for i in range(len(nstr)-1):
            if nstr[i] in digits:
                case3 += sum(d<nstr[i+1] for d in digits) * (len(digits) ** (len(nstr)-i-2))
            else:
                break
        if i == len(nstr)-2 and nstr[i+1] in digits: 
            case3 += 1# this accounts for the equal case, which means you have built exactly the number n

        return case1 + case2 + case3
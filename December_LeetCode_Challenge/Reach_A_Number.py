You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), 
you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].



# O(target^1/2) Time and O(1) Space
class Solution:
    def reachNumber(self, target: int) -> int:
        
        sum_val = 0
        steps = 0
        
        target = abs(target)
        
        while sum_val < target:
            sum_val += steps
            steps += 1
            
        
        while (sum_val - target) % 2 == 1:
            sum_val += steps
            steps += 1
            
        return steps-1


class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2
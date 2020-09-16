Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.


#O(n) Time and O(1) Space
class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            node = root
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
                    
        ans = 0
        for num in nums:
            node = root
            tmp_val = 0
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans, tmp_val)
                                                
        return ans
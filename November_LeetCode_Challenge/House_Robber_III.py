The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) Time and O(n) Space
class Solution:
    mappings = dict()
    def rob(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        if root in self.mappings:
            return self.mappings[root]
        
        val = 0
        
        if root.left is not None:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        
        if root.right is not None:
            val += self.rob(root.right.left) + self.rob(root.right.right)
            
        
        self.mappings[root] = max(root.val+val, self.rob(root.left) + self.rob(root.right))
        
        return self.mappings[root]
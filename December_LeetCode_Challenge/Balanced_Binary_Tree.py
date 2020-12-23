Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node 
differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# O(n) Time and O(h) Space
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        
        def helper(node):
            
            if not node:
                return (0, True)
            
            else:
                
                left_height, is_left_balanced = helper(node.left)
                right_height, is_right_balanced = helper(node.right)
                
                is_balanced = (abs(left_height - right_height) <= 1) and is_left_balanced and is_right_balanced
                
                height = max(left_height, right_height) + 1
                
                return (height, is_balanced)
            
        return helper(root)[1]
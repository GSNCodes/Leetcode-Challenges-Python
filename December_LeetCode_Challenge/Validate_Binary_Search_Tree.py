Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node-s key.
The right subtree of a node contains only nodes with keys greater than the node-s key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node-s value is 5 but its right child-s value is 4.
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) Time and O(n) Space
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        return self.helper(root, None, None)
    
    def helper(self, node, max_val, min_val):
        
        if node is None:
            return True
        
        
        if (max_val is not None and node.val >= max_val) or (min_val is not None and node.val <= min_val):
            return False
        
        else:
            return self.helper(node.left, node.val, min_val) and self.helper(node.right, max_val, node.val)
        
        
# Alternate Solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
            
        stack = [(root, -math.inf, math.inf)] 

        while stack:
            root, lower, upper = stack.pop()

            if not root:
                continue

            val = root.val
            
            if val <= lower or val >= upper:
                return False


            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))

        
        return True 
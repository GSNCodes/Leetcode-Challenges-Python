Given a binary tree, each node has value 0 or 1.  
Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, 
which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Example 1:

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 
Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

Hint #1  
Find each path, then transform that path to an integer in base 10.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#My Solution
# O(n) Time and O(h - height of tree - recursion stack) Space
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.result = 0
        
        def dfs(root, val):
            
            if not root:
                return
            
            val += str(root.val)
            
            if not root.left and not root.right:
                self.result += int(val, 2)
                
            
            dfs(root.left, val)
            dfs(root.right, val)
        
        
        if not root:
            return 0
        
        dfs(root, '')
        
        
        return self.result


# Similar Solution
# O(n) Time and O(h - height of tree - recursion stack) Space
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
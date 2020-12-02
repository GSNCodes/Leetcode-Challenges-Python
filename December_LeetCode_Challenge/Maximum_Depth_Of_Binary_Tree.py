Given the root of a binary tree, return its maximum depth.

A binary tree-s maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# O(n) Time and O(n) Space
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        left  = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

# Iterative Solution
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue, count = deque([root]), 0
        if not root: return count
        
        while queue:
            cur_len = len(queue)
            while cur_len:
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                cur_len -= 1
            count += 1
        return count
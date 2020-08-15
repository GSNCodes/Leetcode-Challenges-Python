You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go 
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MySolution:
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def helper(node, sum, count):
            
            if not node:
                return 
            
            path.append(node.val)
            
            helper(node.left, sum, self.count)
            helper(node.right, sum, self.count)
            
            temp = 0
            for i in range(len(path)-1, -1, -1):
                temp += path[i]
                if temp == sum:
                    self.count += 1
                    
            path.pop()
        
        path = list()
        self.count = 0
        helper(root, sum, self.count)
        
        return self.count
                
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(root,curr_sum):
            if not root:
                return
            curr_sum += root.val
            if curr_sum == sum:
                self.count += 1
            self.count += h[curr_sum - sum]
            h[curr_sum] +=  1  
            preorder(root.left,curr_sum)
            preorder(root.right,curr_sum)
            h[curr_sum] -= 1
             
        self.count = 0
        h = defaultdict(int)
        curr_sum = 0
        preorder(root,curr_sum)
        return self.count

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(node, currSum):
            if not node: 
                return 0
            
            currSum += node.val
            count = 0
            
            if currSum - sum in prefixSum:
                count = prefixSum[currSum - sum]
            if currSum in prefixSum:
                prefixSum[currSum] += 1
            else:
                prefixSum[currSum] = 1
            
            count += helper(node.left, currSum)
            count += helper(node.right, currSum)
            prefixSum[currSum] -= 1
            return count
            
        prefixSum = {0: 1}
        if not root: return 0
        return helper(root, 0)
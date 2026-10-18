# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
        
        memo = {}
        
        def helper(start, end):
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            memo[(start, end)] = all_trees
            return all_trees
        
        return helper(1, n)
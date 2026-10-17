# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        path = []

        def dfs(node, remaining):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                if remaining == node.val:
                    result.append(path.copy())
            else:
                new_remaining = remaining - node.val
                dfs(node.left, new_remaining)
                dfs(node.right, new_remaining)
            path.pop()
        dfs(root, targetSum)
        return result


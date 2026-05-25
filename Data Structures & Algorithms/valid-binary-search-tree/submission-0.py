# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lo, hi = float('-inf'), float('inf')

        def dfs(node, lo, hi) -> bool:
            if not node:
                return True
            return (node.val > lo and node.val < hi) and dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
        
        return dfs(root, lo, hi)
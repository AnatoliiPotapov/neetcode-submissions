# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_before = -101
        def dfs(node, max_before):
            if not node:
                return 0
            
            counter = 0
            if node.val >= max_before:
                counter += 1
                max_before = max(max_before, node.val)

            return counter + dfs(node.left, max_before) + dfs(node.right, max_before)
        return dfs(root, max_before)
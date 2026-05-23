# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recursion(root, n):
            if not root:
                return n
            n += 1
            return max(
                recursion(root.left, n),
                recursion(root.right, n),
                n
            )

        return recursion(root, 0)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answ = -1

        def dfs(node):
            if not node:
                return
            if self.count < k:
                dfs(node.left)

                if self.count == k - 1:
                    self.answ = node.val
                self.count += 1

                dfs(node.right)
            else:
                return
        dfs(root)    
        return self.answ

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        levels = []
        while queue:
            size = len(queue)
            current_level = []
            for _ in range(size):
                el = queue.popleft()
                current_level.append(el.val)
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            levels.append(current_level)
        return levels

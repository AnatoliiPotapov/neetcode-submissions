# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        output = []
        while queue:
            l = len(queue)
            for i in range(l):
                el = queue.popleft()
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
                if i == l - 1:
                    output.append(el.val)
        return output        

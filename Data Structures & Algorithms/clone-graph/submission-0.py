"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        map_nodes = {}

        def clone_node(node):
            if not node:
                return None

            if node in map_nodes:
                return map_nodes[node]
            
            new_node = Node(val = node.val)
            map_nodes[node] = new_node

            for nb in node.neighbors:
                new_node.neighbors.append(clone_node(nb))

            return new_node

        return clone_node(node)


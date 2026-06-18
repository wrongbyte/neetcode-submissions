"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        to_visit = deque([root])
        while to_visit:
            level_size = len(to_visit)

            for i in range(level_size):
                curr = to_visit.popleft()

                if i < level_size - 1:
                    curr.next = to_visit[0]
                if curr.left: 
                    to_visit.append(curr.left)
                if curr.right:
                    to_visit.append(curr.right)
        return root
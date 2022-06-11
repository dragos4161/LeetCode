"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Recursive implementation
""""
class Solution(object):
    def preorder(self, root):
        output = []

        def search(node):
            if not node:
                return
            output.append(node.val)
            for c in node.children:
                search(c)

        search(root)
        return output
"""


    #Iterative implementation


if not root:
    return []
q = deque([root])
output = []
while q:
    node = q.popleft()
    output.append(node.val)
    for c in reversed(node.children):
        q.appendleft(c)
return output



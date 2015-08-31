__author__ = 'chyua'

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def bfs(self, root):

        queue = [(root, 0)]
        while queue:
            node, h = queue.pop(0)

            if queue:
                next, nexth = queue[0]

                if h == nexth:
                    node.next = next

            if node.left is not None:
                queue.append((node.left, h + 1))

            if node.right is not None:
                queue.append((node.right, h + 1))

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.bfs(root)
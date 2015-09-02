# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_depth(self, root):
        if root is None:
            return 0

        if root.left is None:
            return self.get_depth(root.right) + 1
        elif root.right is None:
            return self.get_depth(root.left) + 1
        else:
            return min(self.get_depth(root.left), self.get_depth(root.right)) + 1


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_depth(root)
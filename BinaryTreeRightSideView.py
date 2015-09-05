# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, root, depth, res):
        if root is None:
            return

        if depth >= len(res):
            res.append(root.val)

        self.dfs(root.right, depth + 1, res)
        self.dfs(root.left, depth + 1, res)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, 0, res)
        return res

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

r = s.rightSideView(root)
print(r)
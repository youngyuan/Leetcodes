

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, node, count):
        global sum
        if node is None:
            return

        count = count * 10 + node.val
        if node.left is None and node.right is None:
            sum += count
            return

        if node.left is not None:
            self.dfs(node.left, count)
        if node.right is not None:
            self.dfs(node.right, count)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global sum
        sum = 0
        self.dfs(root, 0)
        return sum

s=Solution()
r=TreeNode(1)
r.left=TreeNode(2)
r.right=TreeNode(3)
print(s.sumNumbers(r))

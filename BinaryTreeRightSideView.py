# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bfs(self, root):
        res = []
        if root is None:
            return res

        queue = [(root, 0)]
        while queue:
            (node, h) = queue.pop(0)
            if not queue:
                res.append(node.val)
            else:
                next, nh = queue[0]
                if h != nh:
                    res.append(node.val)
            if node.left is not None:
                queue.append((node.left, h + 1))
            if node.right is not None:
                queue.append((node.right, h + 1))
        return res

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.bfs(root)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

r = s.rightSideView(root)
print(r)
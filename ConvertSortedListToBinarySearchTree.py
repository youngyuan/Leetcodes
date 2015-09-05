# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convert(self, current_head, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        l = self.convert(current_head, start, mid - 1)
        root = TreeNode(current_head[0].val)
        root.left = l
        current_head[0] = current_head[0].next
        r = self.convert(current_head, mid + 1, end)
        root.right = r
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        return self.convert([head], 0, l - 1)

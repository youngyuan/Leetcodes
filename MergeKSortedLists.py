# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappop, heapify, heapreplace
        root = None
        last = None
        h = [(l.val, l) for l in lists if l]

        heapify(h)
        while h:
            v, n = h[0]
            if not n.next:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, n.next))
            if root is None:
                root = last = n
            else:
                last.next = n
                last = last.next
        return root

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        n = len(nums)
        if n <= 0:
            return []
        res = []
        q = deque()
        for i in range(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)
            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])
        return res

s = Solution()
print(s.maxSlidingWindow([9, 3, -1, -3, 5, 3, 6, 7], 3))
print(s.maxSlidingWindow([1, -1], 1))
print(s.maxSlidingWindow([7, 2, 4], 2))
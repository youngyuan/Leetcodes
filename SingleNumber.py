class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for x in nums:
            res ^= x
        return res

s = Solution()
print(s.singleNumber([2, 2, 3, 3, 17]))
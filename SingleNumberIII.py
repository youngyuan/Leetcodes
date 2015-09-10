class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        n = 0
        for x in nums:
            n ^= x

        n &= ~(n - 1)
        for x in nums:
            if x & n:
                res[0] ^= x
            else:
                res[1] ^= x

        return res

s = Solution()
print(s.singleNumber([1, 2, 1, 3, 2, 5]))
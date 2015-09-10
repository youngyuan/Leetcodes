class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0
        for x in nums:
            twos |= ones & x
            ones ^= x
            threes = ~(ones & twos)
            ones &= threes
            twos &= threes
        return ones

s = Solution()
print(s.singleNumber([13,2,3,2,3,2,3]))
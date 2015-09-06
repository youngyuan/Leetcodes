class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 0:
            return []
        output = [1] * n

        from_first = 1
        from_last = 1
        for i in range(n):
            output[i] *= from_first
            from_first *= nums[i]
            output[n - 1 - i] *= from_last
            from_last *= nums[n - 1 - i]
        return output

s = Solution()
r = s.productExceptSelf([1, 2, 3, 4])
print(r)
r = s.productExceptSelf([1, 2, 3, 0])
print(r)

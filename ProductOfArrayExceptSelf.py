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

        first = 1
        for i in range(n - 1):
            first *= nums[i]
            output[i + 1] *= first
        second = 1
        for i in range(n - 1, 0, -1):
            second *= nums[i]
            output[i - 1] *= second
        return output

s = Solution()
r = s.productExceptSelf([1, 2, 3, 4])
print(r)
r = s.productExceptSelf([1, 2, 3, 0])
print(r)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # naive method
        # sorted_nums = sorted(nums)
        #
        # for i in range(len(sorted_nums) - 1):
        #     if sorted_nums[i] == sorted_nums[i + 1]:
        #         return True
        #
        # return False

        #
        # use dict
        d = dict()
        for x in nums:
            if x not in d:
                d[x] = 0
            else:
                return True
        return False

s = Solution()
r = s.containsDuplicate([1, 2, 3, 1])
print(r)
r = s.containsDuplicate([1, 2, 3, 4])
print(r)
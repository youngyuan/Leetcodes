class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        res = []
        for i in range(0, len(sorted_nums) - 2):
            if i != 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            l, r = i + 1, len(sorted_nums) - 1
            while l < r:
                s = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
        return res

s=Solution()
r=s.threeSum([-1, 0, 1, 2, -1, -4])
print(r)
r=s.threeSum([0, 0, 0, 0])
print(r)
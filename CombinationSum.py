class Solution(object):
    def dfs(self, nums, start, target, result, path):
        if target == 0:
            result.append(path)

        if target > 0:
            for i in range(start, len(nums)):
                self.dfs(nums, i, target - nums[i], result, path + [nums[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        orderNums = sorted(candidates)
        result = []

        self.dfs(orderNums, 0, target, result, [])
        return result
            

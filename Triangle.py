class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        dp = list(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]
            for j in range(len(row)):
                dp[j] = min(dp[j] + row[j], dp[j + 1] + row[j])

        return dp[0]

s = Solution()
r = s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print(r)
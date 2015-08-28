class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        if n < 2:
            return 1

        one = 1
        two = 1
        res = 1

        i = 2
        while i <= n:
            res = one + two
            one = two
            two = res
            i += 1

        return res

s=Solution()
r=s.climbStairs(4)
print(r)
r=s.climbStairs(35)
print(r == 14930352)
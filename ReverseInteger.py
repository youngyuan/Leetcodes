class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = -x
        res = 0
        while x > 0:
            res = res*10 + x % 10
            x //= 10

        if res > 2147483647:
            return 0

        return -res if neg else res

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))

class Solution(object):
    def computeDigitSquare(self, n):
        res = 0
        x = n
        while x > 0:
            res += (x % 10) ** 2
            x //= 10

        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        d = dict()
        while n != 1:
            if n in d:
                return False
            d[n] = 0
            n = self.computeDigitSquare(n)

        return True


s = Solution()
print(s.isHappy(19))
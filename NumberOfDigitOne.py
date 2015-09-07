class Solution(object):
    def brute(self, n):
        count = 0
        for i in range(n + 1):
            while i > 0:
                r = i % 10
                if r == 1:
                    count += 1
                i //= 10
        return count

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones

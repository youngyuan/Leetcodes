class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ['' for _ in range(numRows)]
        line = 0
        change = 1
        for c in s:
            res[line] += c
            line = (line + change) % numRows
            if line == numRows - 1 or line == 0:
                change = -change

        return ''.join(res)



s = Solution()
r = s.convert("PAYPALISHIRING", 3)
print('r = %s, it should be PAHNAPLSIIGYIR, %r' % (r, r == 'PAHNAPLSIIGYIR'))
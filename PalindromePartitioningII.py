class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s);
        if n <= 1:
            return 0

        min_cuts = [i - 1 for i in range(n + 1)]

        for i in range(1, n):
            j = 0
            # odd-length substrings
            while i - j >= 0 and (i + j) < n and s[i - j] == s[i + j]:
                min_cuts[i + j + 1] = min(min_cuts[i +j + 1], 1 + min_cuts[i - j])
                j += 1
            j = 0
            # even-length substrings
            while i - j - 1 >= 0 and (i + j) < n and s[i -j - 1] == s[i + j]:
                min_cuts[i + j + 1] = min(min_cuts[i +j + 1], 1 + min_cuts[i - j - 1])
                j += 1

        return min_cuts[n];

s = Solution()
r = s.minCut("ab")
print(r)
r = s.minCut("aaabaaa")
print(r)
r = s.minCut("aaabaa")
print(r)
r = s.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")
print(r == 75)
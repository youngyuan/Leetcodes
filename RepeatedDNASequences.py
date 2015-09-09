class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        d = dict()
        val = 0
        res = []
        for x in range(len(s)):
            val = (val << 2) + m[s[x]]
            if x < 9:
                continue

            # only keep 20 bits
            val &= (1 << 20) - 1

            d[val] = d.get(val, 0) + 1
            if d[val] == 2:
                res.append(s[x - 9: x + 1])
        return res

s = Solution()
r = s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(r)
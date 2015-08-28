class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        d = dict()
        start = 0
        for i, ch in enumerate(s):
            if ch in d and d[ch] >= start:
                start = d[ch] + 1

            d[ch] = i
            if (i - start + 1) > l:
                l = i - start + 1

        return l


s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))

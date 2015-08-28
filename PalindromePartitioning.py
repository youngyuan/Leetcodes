class Solution(object):
    def isPalindrome(self, s, start, end):
        i = start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, s, start, end, res, path):
        if start > end:
            res.append(path)
            return

        #i is the first substring length
        for i in range(start + 1, end + 2):
            if self.isPalindrome(s, start, i - 1):
                self.dfs(s, i, end, res, path + [s[start:i]])

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, 0, len(s) - 1, res, [])
        return res

s=Solution()
print(s.partition("aab"))
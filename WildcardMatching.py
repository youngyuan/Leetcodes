class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)

        s_start = p_start = s_prev = 0
        star = -1
        while s_start < s_len:
            if p_start < p_len and (p[p_start] == '?' or p[p_start] == s[s_start]):
                p_start += 1
                s_start += 1
            elif p_start < p_len and p[p_start] == '*':
                star = p_start
                s_prev = s_start
                p_start += 1
            elif star != -1:
                p_start = star + 1
                s_prev += 1
                s_start = s_prev
            else:
                return False

        while p_start < p_len and p[p_start] == '*':
            p_start += 1
        return p_start == p_len

s = Solution()
print(s.isMatch("aa","a") is False)
print(s.isMatch("aa","aa") is True)
print(s.isMatch("aaa","aa") is False)
print(s.isMatch("aa", "*") is True)
print(s.isMatch("aa", "a*") is True)
print(s.isMatch("ab", "?*") is True)
print(s.isMatch("aab", "c*a*b") is False)
print(s.isMatch("", "*") is True)
print(s.isMatch("", "*a*") is False)
print(s.isMatch("aac", "*ac"))

print(s.isMatch(
    "bbaaaabababaaabaabbabaabababaaabbaaaababbbbbbbbbaabbaababbaababbabbaabbbabababbababbaaaabaababaabbababbaabbabaaabaabaabaabbabbaaaababaaaabababbbbbabbabbbababbabbabbabbabbbbababaabaaababbaaabaabbbbbaaa",
    "bb*a*bbbb**ab***b**aba*aa**b*a*ab*aa**baaaab***ab*a*****bb*ab*a*ab****a**ab**a*a***bab*b**b*bb***abbabb"))

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs.append(signs[-1] * (-1 if c == '-' else 1))
            elif c == ')':
                signs.pop()
            i += 1
        return total

sol = Solution()
print(sol.calculate("1 + 1") == 2)
print(sol.calculate(" 2-1 + 2 ") == 3)
print(sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23)
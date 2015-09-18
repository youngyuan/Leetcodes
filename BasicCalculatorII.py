class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        tokens = iter(re.findall('\d+|\S', s))
        total, sign = 0, 1
        for token in tokens:
            if token in '+-':
                total += sign * term
                sign = 1 if token == '+' else -1
            elif token in '*/':
                n = int(next(tokens))
                term = term * n if token == '*' else term // n
            else:
                term = int(token)
        return total + sign * term

s = Solution()
print(s.calculate("3+2*2") == 7)
print(s.calculate(" 3/2 ") == 1)
print(s.calculate(" 3+5  / 2 ") == 5)
print(s.calculate("1+1+1") == 3)
print(s.calculate("14-3/2") == 13)
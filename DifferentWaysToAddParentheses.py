class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n


s = Solution()
r = s.diffWaysToCompute("2-1-1")
print('r should be [0,2], %r' % (r))
r = s.diffWaysToCompute("2*3-4*5")
print('r should be [-34, -14, -10, -10, 10], %r' % r)


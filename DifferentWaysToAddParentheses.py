class Solution(object):
    def recurse(self, nums, operators):
        if not operators:
            return nums

        res = []
        for i, o in enumerate(operators):
            left_operators = operators[0: i]
            left_nums = nums[0: i + 1]

            right_operators = operators[i + 1:]
            right_nums = nums[i + 1:]

            left_res = self.recurse(left_nums, left_operators)
            right_res = self.recurse(right_nums, right_operators)

            for x in left_res:
                for y in right_res:
                    if o == '-':
                        n = x - y
                    elif o == '+':
                        n = x + y
                    else:
                        n = x * y
                    res.append(n)
        return res


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re
        tokens = re.split('(\D)', input)
        nums = [int(x) for x in tokens[::2]]
        ops = tokens[1::2]

        return self.recurse(nums, ops)


s = Solution()
r = s.diffWaysToCompute("2-1-1")
print('r should be [0,2], %r' % (r))
r = s.diffWaysToCompute("2*3-4*5")
print('r should be [-34, -14, -10, -10, 10], %r' % (r))


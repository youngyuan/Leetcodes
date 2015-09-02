# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # sort the list
        sorted_list = sorted(intervals, key=lambda interval: interval.start)
        # add the first interval
        res = []
        for i in sorted_list:
            if len(res) == 0:
                res.append(i)
            else:
                l = res[-1]
                if i.start > l.end:
                    res.append(i)
                else:
                    l.end = max(l.end, i.end)
        return res


test_intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
s = Solution()
r = s.merge(test_intervals)
for x in r:
    print('[%d : %d]' % (x.start, x.end))

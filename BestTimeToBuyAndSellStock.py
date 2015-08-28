class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = None
        m = 0
        for x in prices:
            if low is None:
                low = x

            if x - low > m:
                m = x - low
            elif x < low:
                low = x
        return m

s=Solution()
r=s.maxProfit([6,1,3,2,4,7])
print(r)
r=s.maxProfit([2,1,2,1,0,1,2])
print(r)
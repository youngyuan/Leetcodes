class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        #use binary search
        i = 0
        j = m * n - 1
        while i <= j:
            mid = i + (j - i) // 2
            row = mid // n
            col = mid % n
            x = matrix[row][col]
            if target < x:
                j = mid - 1
            elif target > x:
                i = mid + 1
            else:
                return True
        return False

s=Solution()
m=[[1,2,3], [6, 7, 9], [23, 25 ,29],[71, 99, 111]]
print(s.searchMatrix(m, 8))
print(s.searchMatrix(m, 23))
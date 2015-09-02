class Solution(object):
    def dfs(self, grid, row, col, seen):
        if grid[row][col] == '0' or seen[row][col]:
            return
        else:
            seen[row][col] = True

        m = len(grid)
        n = len(grid[0])
        # try the left one
        if col != 0:
            self.dfs(grid, row, col - 1, seen)
        if col < n - 1:
            self.dfs(grid, row, col + 1, seen)
        if row != 0:
            self.dfs(grid, row - 1, col, seen)
        if row < m - 1:
            self.dfs(grid, row + 1, col, seen)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0:
            return 0

        n = len(grid[0])

        seen = [[False] * n for i in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not seen[i][j]:
                    self.dfs(grid, i, j, seen)
                    count += 1
        return count

s = Solution()
g = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
r = s.numIslands(g)
print(r)
g = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
r = s.numIslands(g)
print(r)
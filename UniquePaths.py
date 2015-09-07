class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}

    def uniquePaths(self, m, n):
        board = [[0 for j in range(n)] for i in range(m)]

        for j in range(n):
            board[0][j] = 1
        for i in range(m):
            board[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]

        return board[m-1][n-1]

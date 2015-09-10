class Solution(object):
    def dfs(self, bs, blanks, board):
        if not blanks:
            return True

        i, j = blanks[-1]
        for n in range(9):
            row = i
            col = 9 + j
            mi = 18 + (i // 3) * 3 + (j // 3)
            if bs[row][n] or bs[col][n] or bs[mi][n]:
                continue
            bs[row][n] = bs[col][n] = bs[mi][n] = True
            if self.dfs(bs, blanks[:-1], board):
                board[i][j] = str(n + 1)
                return True
            else:
                bs[row][n] = bs[col][n] = bs[mi][n] = False
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        bs = [[False for __ in range(9)] for _ in range(27)]
        blanks = []
        # init the dict
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blanks.append((i, j))
                    continue
                n = int(board[i][j])
                row = i
                col = 9 + j
                mi = 18 + (i // 3) * 3 + (j // 3)
                bs[row][n - 1] = bs[col][n - 1] = bs[mi][n - 1] = True
        self.dfs(bs, blanks, board)

s = Solution()

startboard = [[] for _ in range(9)]
startboard[0] = ['5', '3', '.', '.', '7', '.', '.', '.', '.']
startboard[1] = ['6', '.', '.', '1', '9', '5', '.', '.', '.']
startboard[2] = ['.', '9', '8', '.', '.', '.', '.', '6', '.']
startboard[3] = ['8', '.', '.', '.', '6', '.', '.', '.', '3']
startboard[4] = ['4', '.', '.', '8', '.', '3', '.', '.', '1']
startboard[5] = ['7', '.', '.', '.', '2', '.', '.', '.', '6']
startboard[6] = ['.', '6', '.', '.', '.', '.', '2', '8', '.']
startboard[7] = ['.', '.', '.', '4', '1', '9', '.', '.', '5']
startboard[8] = ['.', '.', '.', '.', '8', '.', '.', '7', '9']

s.solveSudoku(startboard)
answer = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
          ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
          ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
          ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
          ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
          ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
          ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
          ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
          ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
print(startboard == answer)

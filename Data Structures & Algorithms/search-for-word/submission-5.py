class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if (i < 0 or i >= n or j < 0 or j >= m or
                word[k] != board[i][j] or board[i][j] == '#'):
                return False

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            result = False

            board[i][j] = '#'
            for d in directions:
                if backtrack(i + d[0], j + d[1], k + 1) == True:
                    result = True
            board[i][j] = word[k]
            
            return result

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True

        return False


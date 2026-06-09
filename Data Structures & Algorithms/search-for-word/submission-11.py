class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i == n or j < 0 or j == m or board[i][j] != word[k] or board[i][j] == '#':
                return False

            result = False

            board[i][j] = '#'

            for d in directions:
                if backtrack(i + d[0], j + d[1], k + 1):
                    result = True

            board[i][j] = word[k]

            return result

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0) == True:
                    return True

        return False
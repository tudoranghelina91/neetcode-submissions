class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word):
        crt = self
        for c in word:
            if c not in crt.children:
                crt.children[c] = TrieNode()
            
            crt = crt.children[c]
        crt.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        root = TrieNode()
        visit, res = set(), set()
        
        for w in words:
            root.insert(w)

        def backtrack(i, j, crt, word):
            if i < 0 or i == n or j < 0 or j == m or (i, j) in visit or board[i][j] not in crt.children:
                return 

            visit.add((i, j))
            crt = crt.children[board[i][j]]
            word += board[i][j]
            
            if crt.isWord:
                res.add(word)

            for x, y in directions:
                backtrack(i + x, j + y, crt, word)

            visit.remove((i, j))

        for i in range(n):
            for j in range(m):
                backtrack(i, j, root, "")

        return list(res)
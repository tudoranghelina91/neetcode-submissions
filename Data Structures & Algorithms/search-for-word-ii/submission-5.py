class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        crt = self
        for c in word:
            if c not in crt.children:
                crt.children[c] = TrieNode()
            crt = crt.children[c]
        crt.isWord = True
    


class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if  r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            for d in directions:
                dfs(r + d[0], c + d[1], node, word)
            
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
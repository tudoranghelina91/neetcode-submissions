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

        visit, result = set(), set()
        n, m = len(board), len(board[0])

        def backtrack(i, j, node, word):
            if i < 0 or i == n or j < 0 or j == m or (i, j) in visit or board[i][j] not in node.children:
                return
            
            visit.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.isWord:
                result.add(word)

            for x, y in directions:
                backtrack(i + x, j + y, node, word)

            visit.remove((i, j))

        for i in range(n):
            for j in range(m):
                backtrack(i, j, root, "")

        return list(result)
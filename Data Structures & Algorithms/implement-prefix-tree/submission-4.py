class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        crt = self.root
        for c in word:
            if c not in crt.children:
                crt.children[c] = TreeNode()
            crt = crt.children[c]
        
        crt.endOfWord = True

    def search(self, word: str) -> bool:
        crt = self.root
        for c in word:
            if c not in crt.children:
                return False
            crt = crt.children[c]
        
        return crt.endOfWord

    def startsWith(self, prefix: str) -> bool:
        crt = self.root
        for c in prefix:
            if c not in crt.children:
                return False
            crt = crt.children[c]

        return True
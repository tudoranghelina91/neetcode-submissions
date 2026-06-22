class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crt = self.root
        for c in word:
            if c not in crt.children:
                crt.children[c] = TrieNode()
            crt = crt.children[c]

        crt.isWord = True
            
    def search(self, word: str) -> bool:
        crt = self.root
        for c in word:
            if c not in crt.children:
                return False
            crt = crt.children[c]
        return crt.isWord
        
    def startsWith(self, prefix: str) -> bool:
        crt = self.root
        for c in prefix:
            if c not in crt.children:
                return False
            crt = crt.children[c]
        
        return True
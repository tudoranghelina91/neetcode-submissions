class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        crt = self.root
        for c in word:
            if c not in crt.children:
                crt.children[c] = TrieNode()
            crt = crt.children[c]
        crt.word = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            crt = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in crt.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in crt.children:
                        return False
                    crt = crt.children[c]
            
            return crt.word
            
        return dfs(0, self.root)
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
                
                if c != '.' and c not in crt.children:
                    return False
                
                elif c != '.':
                    crt = crt.children[c] # do normal search

                else:
                    for child in crt.children.values(): # do dfs search if crt char is dot
                        if dfs(i + 1, child):
                            return True
                    return False
            
            return crt.word
            
        return dfs(0, self.root)
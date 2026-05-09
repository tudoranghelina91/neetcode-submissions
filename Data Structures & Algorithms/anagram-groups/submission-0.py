class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for s in strs:
            key = {}
            slist = list(s)
            slist.sort()
            for c in slist:
                if c in key:
                    key[c] += 1
                    continue
                key[c] = 1

            keystr = ""

            for k, v in key.items():
                keystr += (k + str(v))

            if keystr not in hashmap:
                hashmap[keystr] = []
            
            hashmap[keystr].append(s)

        output = []

        for k, v in hashmap.items():
            output.append(v)

        return output
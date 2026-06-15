"""
Build key by counting char occurences - construct key in format a3b5z2
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            occ = [0] * (ord('z') - ord('a') + 1)
            
            for c in s:
                occ[ord(c) - ord('a')] += 1

            key = ""

            for i in range(len(occ)):
                key = key + chr(i + ord('a')) + str(occ[i]) if occ[i] > 0 else key + ""

            hashmap[key] = hashmap.get(key, [])
            hashmap[key].append(s)

        result = []

        for key in hashmap:
            result.append(hashmap[key])

        return result
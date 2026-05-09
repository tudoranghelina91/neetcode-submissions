"""
Build key by counting char occurences - construct key in format a3b5z2
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for s in strs:
            freq = [0] * ((ord('z') - ord('a')) + 1)

            for c in s:
                freq[ord(c) - ord('a')] += 1

            key = ""

            for i in range(len(freq)):
                if freq[i] > 0:
                    key = key + str(chr(i)) + str(freq[i])

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(s)

        output = []

        for k, v in hashmap.items():
            output.append(v)

        return output
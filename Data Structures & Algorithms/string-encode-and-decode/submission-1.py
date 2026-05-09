"""
Encode function will encode the string using string length followed by #
- e.g. 4#Abba

Decode function will loop through the string using two pointers
While iterating with first pointer i, we use an inner loop to look for the # character
Occurence of "#" means we found the start of the string
We use the range of i and j to find the number representing the length of the string
We append to the result array starting from j to j + length
We increment the i pointer
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
           out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while (i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return res

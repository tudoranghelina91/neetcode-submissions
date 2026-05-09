class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = ord('a')
        z = ord('z')
        freq = [0] * ((z - a) + 1)

        for c in s:
            freq[ord(c) - a] += 1

        for c in t:
            freq[ord(c) - a] -= 1

        print(freq)

        for f in freq:
            if f != 0:
                return False
        
        return True
class Solution:
    """
    Hashset. Iterate and remove occurences of current characters from the set
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        n = len(s)
        l = 0
        res = 0

        for r in range(n):
            while (s[r] in sset):
                sset.remove(s[l])
                l += 1

            sset.add(s[r])
            res = max(res, r - l + 1)

        return res
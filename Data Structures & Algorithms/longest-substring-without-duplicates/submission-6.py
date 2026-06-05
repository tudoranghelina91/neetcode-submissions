class Solution:
    """
    Hashset. Iterate and remove occurences of current characters from the set
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        resset = set()
        n = len(s)
        l = 0
        result = 0

        for r in range(n):
            while s[r] in resset:
                resset.remove(s[l])
                l += 1

            result = max(result, r - l + 1)

            resset.add(s[r])

        return result
class Solution:
    """
    Hashset. Iterate and remove occurences of current characters from the set
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        l = 0
        n = len(s)
        result = 0

        for r in range(n):
            while s[r] in res_set:
                res_set.remove(s[l])
                l += 1

            res_set.add(s[r])
            
            result = max(result, r - l + 1)

        return result
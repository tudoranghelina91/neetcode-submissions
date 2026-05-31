class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        n = len(s)
        result = 0
        maxf = 0

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            if r - l + 1 - maxf <= k:
                result = max(result, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return result
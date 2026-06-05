class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        n = len(s)
        maxf = 0
        result = 0

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            if r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1

            else:
                result = r - l + 1

        return result            
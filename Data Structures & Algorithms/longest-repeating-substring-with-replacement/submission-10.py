class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        maxf = 0
        l = 0
        res = 0

        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])

            if r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)

        return res
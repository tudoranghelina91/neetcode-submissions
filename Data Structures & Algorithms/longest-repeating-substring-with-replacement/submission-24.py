class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        n = len(s)
        result = 0

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            if r - l + 1 - maxf > k:
                # I always mix the two lines below - we decrement the counter then increment the pointer
                count[s[l]] -= 1
                l += 1
                continue

            result = r - l + 1

        return result
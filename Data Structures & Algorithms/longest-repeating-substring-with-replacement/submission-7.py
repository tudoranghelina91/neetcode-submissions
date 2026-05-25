class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        maxf = 0
        result = 0
        l = 0

        for r in range(n):
            f = freq.get(s[r], 0) + 1
            freq[s[r]] = f
            maxf = max(maxf, freq[s[r]])
            
            if r - l + 1 - maxf <= k:
                result = max(result, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
                
        return result
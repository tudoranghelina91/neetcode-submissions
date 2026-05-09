class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        n = len(s)
        j = n - 1

        while j > i and i < n:
            while i < n and not s[i].isalnum():
                i += 1
            
            while j >= 0 and not s[j].isalnum():
                j -= 1

            if i < n and j >= 0 and s[i].lower() != s[j].lower():
                return False
            
            j -= 1
            i += 1

        return True
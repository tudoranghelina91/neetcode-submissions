class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()
        i = 0
        n = len(s)
        j = n - 1

        while j > i and i < n:
            while i < n and not l[i].isalnum():
                i += 1
            
            while j >= 0 and not l[j].isalnum():
                j -= 1

            if i < n and j >= 0 and l[i] != l[j]:
                return False
            
            j -= 1
            i += 1

        return True
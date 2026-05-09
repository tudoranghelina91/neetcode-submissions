class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        n = len(s)
        j = n - 1

        while j > i and i < n:
            while i < n and not self.isalphanumeric(s[i]): # can use isalnum too if allowed
                i += 1
            
            while j >= 0 and not self.isalphanumeric(s[j]):
                j -= 1

            if i < n and j >= 0 and s[i].lower() != s[j].lower():
                return False
            
            j -= 1
            i += 1

        return True

    def isalphanumeric(self, char):
        return ord('A') <= ord(char) <= ord('Z') or \
        ord('a') <= ord(char) <= ord('z') or \
        ord('0') <= ord(char) <= ord('9')
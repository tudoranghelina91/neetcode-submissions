class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
                continue
            if len(stack) > 0 and (p == ')' and stack[-1] == '(' or p == ']' and stack[-1] == '[' or p == '}' and stack[-1] == '{'):
                stack.pop()
                continue
            
            stack.append(p)

        return len(stack) == 0
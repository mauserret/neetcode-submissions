class Solution:
    def isValid(self, s: str) -> bool:
        open_b = {"(":0, "[":1, "{":2}
        closed_b = {")":0, "]":1, "}":2}
        stack = []
        for i in range(len(s)):
            if s[i] in open_b:
                stack.append(open_b[s[i]])
            elif s[i] in closed_b:
                if not stack or stack[-1] != closed_b[s[i]]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False        
            
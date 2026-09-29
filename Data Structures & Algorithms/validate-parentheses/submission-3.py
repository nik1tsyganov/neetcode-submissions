class Solution:
    def isValid(self, s: str) -> bool:
        works = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char in works.keys():
                if stack and stack[-1] == works[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
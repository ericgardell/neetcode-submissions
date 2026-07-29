class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        open_chars = {"(", "{", "["}
        matches = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for char in s:
            if char in open_chars:
                stack.append(char)
            else:
                if not stack:
                    return False

                opening = stack.pop()

                if matches[opening] != char:
                    return False

        return not stack
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        openChars = set(['(',  '{',  '[' ])
        matches = {'(': ')', '{': '}', '[': ']'}
        if not s[0] in openChars or len(s) % 2 != 0: 
            return False

        for i in range(len(s)):
            print(i, s[i], stack, 'open' if s[i] in openChars else 'close')
            if s[i] in openChars:
                stack.append(s[i])
                print('\t', stack)
            elif not stack:
                print(f"\t{i}")
                return False
            else: # does match
                prev = stack.pop()
                print(prev, matches[prev])
                if not matches[prev] == s[i]:
                    return False
        stackIsEmpty = stack==False
        print(f"escaped loop: stack:{stack} | stackIsEmpty:{stackIsEmpty}")
        if stack:
            return False
        return True

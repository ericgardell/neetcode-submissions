import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(s)
        s = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)

        # print(cleaned)
        l, r = 0, len(cleaned)-1

        while l < r:
            if cleaned[l] != cleaned[r]: 
                # print(l, r, cleaned[l], cleaned[r], ord(cleaned[l]), ord(cleaned[r]))
                return False
            l += 1
            r -= 1
        return True
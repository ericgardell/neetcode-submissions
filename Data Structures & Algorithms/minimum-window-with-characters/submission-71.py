from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        needed = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(needed)

        left = 0
        best_left = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            window[char] += 1

            # This character has just reached its required count.
            if char in needed and window[char] == needed[char]:
                have += 1

            # Current window contains everything required.
            while have == need:
                window_length = right - left + 1

                if window_length < best_length:
                    best_left = left
                    best_length = window_length

                left_char = s[left]
                window[left_char] -= 1

                # Removing this character made the window invalid.
                if (
                    left_char in needed
                    and window[left_char] < needed[left_char]
                ):
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]
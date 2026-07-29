from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        needed_counts = Counter(t)
        search_counts = Counter()

        left = 0
        best_left = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            # Expand the window.
            search_counts[char] += 1

            # Contract while the current window is valid.
            while not (needed_counts - search_counts):
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left

                # Remove the character currently at left,
                # then advance left.
                left_char = s[left]
                search_counts[left_char] -= 1

                if search_counts[left_char] == 0:
                    del search_counts[left_char]

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]
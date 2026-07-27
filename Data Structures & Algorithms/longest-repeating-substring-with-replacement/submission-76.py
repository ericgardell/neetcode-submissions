class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right, char in enumerate(s):
            frequencies[char] = frequencies.get(char, 0) + 1
            max_frequency = max(max_frequency, frequencies[char])

            window_length = right - left + 1

            while window_length - max_frequency > k:
                frequencies[s[left]] -= 1
                left += 1
                window_length = right - left + 1

            max_length = max(max_length, window_length)

        return max_length
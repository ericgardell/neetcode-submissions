class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def windowIsValid(s: str, left: int, right: int) -> bool:
            freqs = {}
            for i in range(left, right+1):
                freqs[s[i]] = freqs.get(s[i], 0) + 1
            max_freq = max(freqs.values()) if freqs.values() else 0
            curr_total = (1+(right-left) - max_freq)
            # print(f"\t{"✓" if curr_total <= k else "X"}  |  1+({right}-{left}) - {max_freq} = {curr_total}  |  {freqs.items()}")
            return curr_total <= k
            
        left, right = 0, 1
        substrings = {s[left]: (left, right, k)} # char: (start_idx, end_idx, allowance)
        maxLen = min(len(s), k)
        while right < len(s):
            char = s[right]
            # print(f"L:{left}-R:{right} {char} | {s[left:right+1]}")
            isValid = windowIsValid(s, left, right)
            
            if isValid:
                windowLength = right - left +1
                maxLen = max(maxLen, windowLength)
                right += 1
            else:
                print("\tshrinking from left")
                left += 1

        return maxLen
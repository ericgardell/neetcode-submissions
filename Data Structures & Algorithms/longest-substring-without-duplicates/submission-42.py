class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left, right = 0, 1
        seen = set(s[left])
        longest = 1
        # expand rightwards until char is in the set
        # then contract from left side until its not anymore and then keep going
        while right < len(s): 
            # rightward expansion
            char = s[right]
            start = s[left]
            print(f"{left}/{right} {char} | {s[left:right]}")
            if char in seen:
                seen = set(s[left:right+1]) # reset the set
                while start != char and left < right: 
                    left += 1
                    start = s[left]
                    print(f"\tcontracting, {left}/{right} | {s[left:right+1]}")
                    seen = set(s[left:right+1]) # reset the set
                print(f"\t{left}/{right} {char}: resetting seen to {s[left:right+1]}, longest now {max(longest, len(seen))}")
            else:
                print(f"\t{left}/{right}: adding {char} to {s[left:right+1]}, longest now {max(longest, len(seen))}")
                seen.add(char)
            longest = max(longest, len(seen))
            right += 1
        return longest
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)-1
        sorted_search = sorted(s1)
        print(left, right, sorted_search, s2[left:right+1])
        while right < len(s2):
            # print(f"{left}-{right} | {sorted_search} vs {sorted(s2[left:right+1])}")
            if sorted_search==sorted(s2[left:right+1]):
                return True
            right += 1
            left += 1
        return False
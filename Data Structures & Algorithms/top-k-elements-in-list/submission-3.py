from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        print(freqs)
        return [f[0] for f in freqs.most_common(k)]

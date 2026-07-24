class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) <= 1:
            return len(nums)
        nums = sorted(list(set(nums)))
        longest = 1
        seq = [nums[0]]
        l,r = 0,1
        while r < len(nums):

            if seq[-1] +1 == nums[r]:
                seq.append(nums[r])
                longest = max(longest, len(seq))
            else:
                l = r
                seq = [nums[l]]
            r += 1
        return longest 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) <= 1:
            return len(nums)

        nums = sorted(nums)
        seq = [nums[0]]
        heads = {num:{"length":1, "tail":num} for num in nums}
        for i in range(1, len(nums)):
            current = nums[i]
            target = current - 1
            matching_heads = [k for k,v in heads.items() if v["tail"]==target]
            print(f"i:{i}, current:{current}, target:{target}, matches:{matching_heads}")
            for match in matching_heads:
                heads[match] = {"length":heads[match]["length"]+1, "tail":current}
        

        return max([v['length'] for v in heads.values()])
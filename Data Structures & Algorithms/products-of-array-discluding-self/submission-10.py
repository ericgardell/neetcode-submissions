class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return [nums[1], nums[0]]

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        print("input:", nums)
        prefix[1] = nums[0]
        suffix[-2] = nums[-1]
        for p in range(2, len(nums)):
            prefix[p] = prefix[p-1] * nums[p-1]
        print("prefixes", prefix)
        
        for s in range(len(nums)-2, -1, -1):
            suffix[s] = suffix[s+1] * nums[s+1]
            print(f"{s}: {suffix[s]} = {suffix[s+1]} * {nums[s+1]}")
        print("suffixes", suffix)

        result = [prefix[i]*suffix[i] for i in range(len(nums))]
        print(result)
        return result
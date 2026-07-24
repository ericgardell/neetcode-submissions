class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return [nums[1], nums[0]]

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        prefix[1] = nums[0]
        suffix[-2] = nums[-1]

        for p in range(2, len(nums)):
            prefix[p] = prefix[p-1] * nums[p-1]
        
        for s in range(len(nums)-2, -1, -1):
            suffix[s] = suffix[s+1] * nums[s+1]

        return [prefix[i]*suffix[i] for i in range(len(nums))]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nested 2-ptr?
        # sets of 3 indices that sum to 0
        nums.sort()
        num_map = [(i,v) for i,v in enumerate(nums)]
        # num_map = sorted(num_map, key=lambda x: x[1])
        res = set()
        for sorted_i in range(len(num_map)-2):
            if sorted_i > 0 and num_map[sorted_i][1] == num_map[sorted_i-1][1]:
                continue
            l,r = sorted_i+1, len(nums)-1
            v = num_map[sorted_i][1]

            while l < r:
                curr = num_map[l][1] + num_map[r][1] + v
                if curr == 0:
                    res.add(tuple(sorted([num_map[l][1], num_map[r][1], v])))
                    l += 1
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return [list(t) for t in res]
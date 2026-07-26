class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # fast-slow ptr?
        area = 0
        l,r = 0, len(heights)-1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            area = max(area, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            print(l, r, curr_area, area)
        return area
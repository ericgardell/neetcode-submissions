class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # iterate through, decide when to bank some area
        left, right = 0, len(height)-1
        left_max = height[left]
        right_max = height[right]
        stored = [0] * len(height)
        while left < right:
            left_height, right_height = height[left], height[right]
            left_max = max(left_max, left_height)
            right_max = max(right_max, right_height)
            
            print(f"left:{left} | right:{right} | left_h:{left_height} | left_max:{left_max} | right_h:{right_height} | right_max:{right_max} | area:{area}")
            
            curr_height = min(left_max, right_max) - left_height
            
            if left_height < right_height:
                area += left_max - height[left]
                left += 1
            else:
                area += right_max - height[right]
                right -= 1
        return area
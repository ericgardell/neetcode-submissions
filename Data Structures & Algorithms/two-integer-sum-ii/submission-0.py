class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while r < len(numbers):
            little = numbers[l]
            big = numbers[r]
            if little + big == target:
                return [l+1, r+1]
            elif little + big < target:
                # too small, increase by moving the left ptr
                l += 1
            else:
                # too big, decrease by moving right ptr
                r -= 1
        return [l+1, r+1]
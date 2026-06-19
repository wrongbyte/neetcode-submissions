class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_decreasing = True
        is_increasing = True

        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > prev and is_decreasing:
                is_decreasing = False
            if nums[i] < prev and is_increasing:
                is_increasing = False
            if not is_increasing and not is_decreasing:
                return False
            prev = nums[i]

        return True
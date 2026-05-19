class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        else:
            values = {}
            for (i, num) in enumerate(nums):
                complement = target - num
                if complement in values:
                    return sorted([i, values[complement]])
                else:
                    values[num] = i
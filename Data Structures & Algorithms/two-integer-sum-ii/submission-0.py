# 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return [numbers[0] + 1, numbers[1] + 1]

        l = 0
        r = len(numbers) - 1

        while r > l:
            result = numbers[l] + numbers[r]
            if result > target:
                r -= 1
                continue
            elif result < target:
                l += 1
                continue
            else:
                break

        return [l + 1, r + 1]

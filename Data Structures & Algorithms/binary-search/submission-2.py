class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while len(nums[l:r+1]) > 1:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
                continue
            elif nums[mid] < target:
                l = mid + 1
                continue
            else: #if equal to mid
                return mid
        if nums[l] == target:
            return l

        return -1
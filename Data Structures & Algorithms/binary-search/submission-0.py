class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0

        while len(nums[l:r+1]) > 1:
            mid = (l + r) // 2
            # print(f"curr mid is {mid} l is {l} r is {r}")
            if nums[mid] > target:
                # print(f"{nums[mid]} is bigger than {target}")
                r = mid - 1
                continue
            elif nums[mid] < target:
                # print(f"{nums[mid]} is smaller than {target}")
                l = mid + 1
                continue
            else: #if equal to mid
                return mid
        # print(f"{l} {r} {nums[l:r+1]}")
        if nums[l] == target:
            return l

        return -1
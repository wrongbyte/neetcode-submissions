class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        first_occurrence = binary_search(nums, target, "first", l, r)
        if first_occurrence == -1: # we didnt found
            return [-1, -1]
        last_occurrence = binary_search(nums, target, "last", l, r)

        return [first_occurrence, last_occurrence]

def binary_search(nums, target, occurrence, l, r) -> int:
    occurrence_idx = -1

    while r >= l:
        mid = (l + r) // 2
        if nums[mid] == target:
            occurrence_idx = mid
            if occurrence == "first":
                r = mid - 1
            if occurrence == "last":
                l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
    return occurrence_idx

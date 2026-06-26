class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurrence = -1
        last_occurrence = -1
        
        l, r = 0, len(nums) - 1
        # search for first occurrence
        print("first occ search")
        while r >= l:
            mid = (l + r) // 2
            print(f"l is {l} r is {r}, mid is {mid}")
            if nums[mid] == target:
                first_occurrence = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if first_occurrence == -1:
            return [-1,-1]

        l, r = 0, len(nums) - 1
        print("last occ search")
        # search for last occurrence
        while r >= l:
            mid = (l + r) // 2
            print(f"l is {l} r is {r}, mid is {mid}")
            if nums[mid] == target:
                last_occurrence = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

        return [first_occurrence, last_occurrence]

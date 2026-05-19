
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for num in nums:
            if not num in values:
                values.add(num)
            else:
                return True
        return False

        
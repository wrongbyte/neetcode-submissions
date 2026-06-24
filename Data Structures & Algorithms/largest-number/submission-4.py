from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sortNumbers(a,b):
            # for each pair of numbers, check what is the
            # biggest number we can get: ab or ba
            opt_1 = str(a) + str(b)
            opt_2 = str(b) + str(a)
            # strings of the same length can be compared w/o converting
            # to int
            if opt_1 > opt_2:
                return -1 # a is greater than b
            elif opt_2 > opt_1:
                return 1 # a is smaller than b
            else:
                return 0
        # the only way 0 can be the greatest element is if all other elements
        # are also 0
        if nums[0] == 0: 
            return "0"

        nums.sort(key=cmp_to_key(sortNumbers))
        return "".join([str(n) for n in nums])

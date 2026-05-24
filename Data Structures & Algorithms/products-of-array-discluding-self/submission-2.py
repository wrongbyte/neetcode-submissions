import math


# First attempt: using division. O(n) schizo solution :p
# here what we do is to handle three cases:
# 1 - all numbers are different from 0
# 2 - there is one zero: in this case, we have n * 0 where n != 0. we compute
#     the value of the product except zero and fill the rest of array with zeroes
# 3 - there is more than one zero: in this case, the product will always be zero so 
#     we return an array containing only zeroes

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        only_zero_index = 0
        prod = 1
        
        for (i, n) in enumerate(nums):
            if n == 0:
                zeroes += 1
                if zeroes == 1:
                    only_zero_index = i
                if zeroes > 1:
                    return [0] * len(nums)
    
        # compute the value for product of array except 0
        if zeroes == 1:
            nums_except_zero = [x for x in nums if x != 0] 
            output = [0] * len(nums)
            output[only_zero_index] = math.prod(nums_except_zero)
            return output

        prod = math.prod(nums)
        output = []

        for n in nums: 
            if n == 0:
                output.append(math.prod(nums_except_zero))
            else: 
                output.append(int(prod / n))
                
        return output

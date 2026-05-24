# solution 1 = using division. ugly solution
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        prod = 1
        
        for n in nums:
            if n == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0] * len(nums)
    
        # compute the value for product of array except 0
        if zeroes == 1:
            nums_except_zero = [x for x in nums if x != 0] 

        print(f"zeroes is {zeroes}")
        prod = math.prod(nums)
        output = []

        for n in nums: 
            if n == 0:
                output.append(math.prod(nums_except_zero))
            else: 
                output.append(int(prod / n))
                
        print(prod) 
        return output

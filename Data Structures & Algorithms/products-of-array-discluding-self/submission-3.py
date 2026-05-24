import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        suffix_arr = []
        output = []
        nums_len = len(nums)

        # create the prefix and suffix arrays: O(n)
        for (i, num) in enumerate(nums):
            if i == 0:
                prefix_arr.append(nums[0])
                suffix_arr.append(nums[nums_len - 1])
            else:
                prefix = nums[i] * prefix_arr[i - 1]
                prefix_arr.append(prefix)

                suffix = nums[nums_len - 1 - i] * suffix_arr[i - 1]
                suffix_arr.append(suffix)
    
        for i in range(nums_len):
            if i == 0:
                output.append(suffix_arr[nums_len - 1 - 1])
            elif i == nums_len - 1:
                output.append(prefix_arr[nums_len - 1 - 1])
            else:
                product = prefix_arr[i - 1] * suffix_arr[nums_len - 1 - i - 1]
                output.append(product)
            
        # print(f"prefix arr is {prefix_arr}")
        # print(f"suffix arr is {suffix_arr}")


        return output

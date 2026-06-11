class Solution:
    # amount of water = min(heights[l], heights[r]) * (r - l)
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(heights) - 1
        while r > l:
            curr_amount = min(heights[l], heights[r]) * (r - l)
            if curr_amount > max_amount:
                max_amount = curr_amount
            if heights[l] >  heights[r]:
                r -= 1
            # we move the pointer that points to the smaller value
            # of the combination
            elif heights[l] <  heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        
        return max_amount
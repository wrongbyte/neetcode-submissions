class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)
        longest = 1
        seen = {}

        for i in nums:
            if i - 1 in seen:
                # we compute the longest sequence ending in i
                curr_seq = seen[i - 1] + 1
                if curr_seq > longest:
                    longest = curr_seq

                seen[i] = curr_seq
            else:
                seen[i] = 1

        return longest
        
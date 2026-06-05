class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set([])
        num_map = {} # numbers and their indices

        # populate map
        for (i, n) in enumerate(nums):
            if not n in num_map:
                num_map[n] = set([i])
            else:
                num_map[n].add(i)
        
        for i in range(len(nums)):
            indexes_used = set([i])
            target = 0 - nums[i]

            # we perform a 2-sum
            for j in range(len(nums)):
                if i == j:
                    continue # skip because they are the same element
                complement = target - nums[j]

                if complement in num_map:
                    if complement == nums[j] or complement == nums[i]:
                        complement_indexes = num_map[complement]
                        filtered = [x for x in num_map[complement] if x != j and x != i]
                    
                        if len(filtered) == 0:
                            continue

                    sorted_triplet = sorted([nums[i], nums[j], complement])
                    triplet = (sorted_triplet[0], sorted_triplet[1], sorted_triplet[2])
                    triplets.add(triplet)

        return [list(t) for t in triplets]

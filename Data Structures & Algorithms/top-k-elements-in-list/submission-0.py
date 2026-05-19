class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for num in nums:
            if not num in elements:
                elements[num] = 1
            else:
                elements[num] += 1
        elements_sorted = dict(sorted(elements.items(), key = lambda item: item[1], reverse=True))
        return list(elements_sorted.keys())[:k]

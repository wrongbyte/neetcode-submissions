class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for row in matrix:
            array += row
        return bin_search(target, array)
    
def bin_search(target: int, arr: List[int]) -> bool:
    l, r = 0, len(arr) - 1
    while r >= l:
        mid = (l + r) // 2
        curr = arr[mid]
        if curr == target:
            return True
        elif curr > target:
            r = mid - 1
        elif curr < target:
            l = mid + 1
    return False
            
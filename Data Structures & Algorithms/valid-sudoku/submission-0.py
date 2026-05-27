# TODO: check edge cases
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        EMPTY = "."
        # for each row, check if there is duplicates
        # for each column check if there is duplicates
        # for each sub-box check if there is duplicates

        rows_values = {}
        columns_values = {}
        
        # boxes = [{0: set(), 1: set(), 2: set()},{3: set(), 4: set(), 5: set()},{6: set(), 7: set(), 8: set()}]
        # boxes_values = {}

        # boxes[0][2] -> box of the first row, third column

        intervals = [set([0,1,2]),set([3,4,5]),set([6,7,8])]
        boxes = [[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]

        for i in range(9):
            rows_values[i] = set()
            columns_values[i] = set()

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != EMPTY:
                    if value in rows_values[i]:
                        return False
                    if value in columns_values[j]:
                        return False
                    
                    i_interval = 0
                    j_interval = 0

                    # this is ugly
                    if i > 2 and i < 6:
                        i_interval = 1
                    elif i > 5:
                        i_interval = 2
                    
                    if j > 2 and j < 6:
                        j_interval = 1
                    elif j > 5:
                        j_interval = 2

                    if value in boxes[i_interval][j_interval]:
                        return False
                    
                    rows_values[i].add(value)
                    columns_values[j].add(value)
                    boxes[i_interval][j_interval].add(value)
                    
        return True
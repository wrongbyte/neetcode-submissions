# TODO: check edge cases
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        EMPTY = "."
        # for each row, check if there is duplicates
        # for each column check if there is duplicates
        # for each sub-box check if there is duplicates

        rows_values = {}
        columns_values = {}

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

                    box_row = i // 3
                    box_col = j // 3

                    if value in boxes[box_row][box_col]:
                        return False
                    
                    rows_values[i].add(value)
                    columns_values[j].add(value)
                    boxes[box_row][box_col].add(value)

        return True
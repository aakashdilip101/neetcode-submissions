class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col == '.':
                    continue

                box_index = (row_index // 3) * 3 + (col_index // 3)
                if col in row_sets[row_index] or col in col_sets[col_index] or col in box_sets[box_index]:
                    return False
                else:
                    row_sets[row_index].add(col)
                    col_sets[col_index].add(col)
                    box_sets[box_index].add(col)
        
        return True
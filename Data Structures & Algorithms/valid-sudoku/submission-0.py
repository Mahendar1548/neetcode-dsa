class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_wise_numbers = defaultdict(set)
        col_wise_numbers = defaultdict(set)
        box_wise_numbers = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                box_number = (i // 3) * 3 + j // 3
                print(box_number)
                if (value in row_wise_numbers[i] or value in col_wise_numbers[j] or 
                        value in box_wise_numbers[box_number]):
                    return False
                row_wise_numbers[i].add(value)
                col_wise_numbers[j].add(value)
                box_wise_numbers[box_number].add(value)
        
        return True
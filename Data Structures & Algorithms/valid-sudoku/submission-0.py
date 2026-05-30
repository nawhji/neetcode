class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(board, i):
            is_exist = [0] * 9
            for x in range(9):
                if board[i][x] != ".":
                    num = int(board[i][x])
                    if is_exist[num-1] == 0:
                        is_exist[num-1] = 1
                    else:
                        return False
            return True
        def check_col(board, i):
            is_exist = [0] * 9
            for x in range(9):
                if board[x][i] != ".":
                    num = int(board[x][i])
                    if is_exist[num-1] == 0:
                        is_exist[num-1] = 1
                    else:
                        return False
            return True
        def check_block(board, i):
            row_pos = (i-1) // 3
            col_pos = (i-1) % 3

            is_exist = [0] * 9
            for x in range(3):
                for y in range(3):
                    if board[row_pos * 3 + x][col_pos * 3 + y] != ".":
                        num = int(board[row_pos * 3 + x][col_pos * 3 + y])
                        if is_exist[num-1] == 0:
                            is_exist[num-1] = 1
                        else:
                            return False
            return True
        
        for i in range(9):
            if not check_row(board, i):
                return False
            if not check_col(board, i):
                return False
            if not check_block(board, i):
                return False
        return True
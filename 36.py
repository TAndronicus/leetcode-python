from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for col in range(9):
        ar = [0] * 9
        for row in range(9):
            if board[row][col] != '.':
                if ar[int(board[row][col]) - 1] == 1:
                    return False
                else:
                    ar[int(board[row][col]) - 1] = 1
    for boxH in range(3):
        for boxV in range(3):
            ar = [0] * 9
            for row in range(3):
                for col in range(3):
                    if board[3 * boxH + row][3 * boxV + col] != '.':
                        if ar[int(board[3 * boxH + row][3 * boxV + col]) - 1] == 1:
                            return False
                        else:
                            ar[int(board[3 * boxH + row][3 * boxV + col]) - 1] = 1
    for row in range(9):
        ar = [0] * 9
        for col in range(9):
            if board[row][col] != '.':
                if ar[int(board[row][col]) - 1] == 1:
                    return False
                else:
                    ar[int(board[row][col]) - 1] = 1
    return True


if __name__ == '__main__':
    print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(not isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

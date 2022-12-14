from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def matrixEmpty():
            return len(matrix) == 0 or len(matrix[0]) == 0

        while True:
            firstRow = matrix.pop(0)
            for el in firstRow:
                yield el
            if matrixEmpty():
                break
            for i in range(len(matrix) - 1):
                yield matrix[i].pop(-1)
            last_row = matrix.pop(-1)
            for el in reversed(last_row):
                yield el
            if matrixEmpty():
                break
            for i in range(len(matrix) - 1, 0, -1):
                yield matrix[i].pop(0)


if __name__ == '__main__':
    s = Solution()
    print(list(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
    print(list(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    print(list(s.spiralOrder([[0]])) == [0])
    print(list(s.spiralOrder([[0, 1, 2, 3]])) == [0, 1, 2, 3])
    print(list(s.spiralOrder([[0], [1], [2], [3]])) == [0, 1, 2, 3])

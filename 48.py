import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for i in range(math.ceil(l / 2)):
            for j in range(math.floor(l / 2)):
                matrix[j][l - 1 - i], matrix[l - 1 - i][l - 1 - j], matrix[l - 1 - j][i], matrix[i][j] = matrix[i][j], matrix[j][l - 1 - i], \
                    matrix[l - 1 - i][l - 1 - j], \
                    matrix[l - 1 - j][i]


if __name__ == '__main__':
    s = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix1)
    print(matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(matrix2)
    print(matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

import math
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 0 - right, 1 - down, 2 - left, 3 - up
        direction, currentPosition, input, result = 0, [0, 0], 1, [[0] * n for _ in range(n)]
        while input <= math.pow(n, 2):
            result[currentPosition[0]][currentPosition[1]] = input
            input += 1
            if direction == 0:
                if currentPosition[1] == n - 1 or result[currentPosition[0]][currentPosition[1] + 1] != 0:
                    direction = (direction + 1) % 4
                    currentPosition[0] += 1
                else:
                    currentPosition[1] += 1
            elif direction == 1:
                if currentPosition[0] == n - 1 or result[currentPosition[0] + 1][currentPosition[1]] != 0:
                    direction = (direction + 1) % 4
                    currentPosition[1] -= 1
                else:
                    currentPosition[0] += 1
            elif direction == 2:
                if currentPosition[1] == 0 or result[currentPosition[0]][currentPosition[1] - 1] != 0:
                    direction = (direction + 1) % 4
                    currentPosition[0] -= 1
                else:
                    currentPosition[1] -= 1
            elif direction == 3:
                if currentPosition[0] == 0 or result[currentPosition[0] - 1][currentPosition[1]] != 0:
                    direction = (direction + 1) % 4
                    currentPosition[1] += 1
                else:
                    currentPosition[0] -= 1
        return result

    def generateMatrix2(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            result[i][j] = k + 1
            if result[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(1) == [[1]])
    print(s.generateMatrix(2) == [[1, 2], [4, 3]])
    print(s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    print(s.generateMatrix2(1) == [[1]])
    print(s.generateMatrix2(2) == [[1, 2], [4, 3]])
    print(s.generateMatrix2(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

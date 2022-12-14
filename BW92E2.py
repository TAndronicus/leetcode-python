from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRows, onesCols = [0] * len(grid), [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    onesRows[i] += 1
                    onesCols[j] += 1
        res = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = 2 * (onesRows[i] + onesCols[j]) - len(grid) - len(grid[0])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
    print(s.onesMinusZeros([[1, 1, 1], [1, 1, 1]]))

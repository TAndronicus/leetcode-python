from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        minSum = [[1] * m for _ in range(n)]
        minSum[0][0] = grid[0][0]
        for i in range(1, m):
            minSum[0][i] = minSum[0][i - 1] + grid[0][i]
        for j in range(1, n):
            minSum[j][0] = minSum[j - 1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                minSum[j][i] = grid[j][i] + min(minSum[j - 1][i], minSum[j][i - 1])
        return minSum[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7)
    print(s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12)
    print(s.minPathSum([[0]]) == 0)

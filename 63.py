from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [[1] * n for _ in range(m)]
        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                ways[i][0] = 0
            else:
                ways[i][0] = ways[i - 1][0]
        for j in range(0, n):
            if obstacleGrid[0][j] == 1:
                ways[0][j] = 0
            else:
                ways[0][j] = ways[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    ways[i][j] = 0
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2)
    print(s.uniquePathsWithObstacles([[0, 1, 0], [0, 1, 0], [0, 0, 0]]) == 1)
    print(s.uniquePathsWithObstacles([[0, 1, 0], [0, 1, 0], [0, 0, 0]]))
    print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1)
    print(s.uniquePathsWithObstacles([[1]]) == 0)

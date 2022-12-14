import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(1, 1) == 1)
    print(s.uniquePaths(3, 7) == 28)
    print(s.uniquePaths(2, 3) == 3)
    print(s.uniquePaths2(1, 1) == 1)
    print(s.uniquePaths2(3, 7) == 28)
    print(s.uniquePaths2(2, 3) == 3)

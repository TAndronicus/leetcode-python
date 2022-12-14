class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * n for _ in range(5)]
        dp[1][0] = 2
        dp[2][0] = 3
        dp[3][0] = 4
        dp[4][0] = 5
        for i in range(1, 5):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[4][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.countVowelStrings(1))
    print(s.countVowelStrings(2))
    print(s.countVowelStrings(33))
    for i in range(1, 51):
        print(str(i) + " -> " + str(s.countVowelStrings(i)) + ",")

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [[0] * 2 for _ in range(high + 1)]
        dp[0][0] = 1
        sum = 0
        for i in range(high + 1):
            if i - zero >= 0:
                dp[i][0] = (dp[i - zero][0] + dp[i - zero][1]) % 1000000007
            if i - one >= 0:
                dp[i][1] = (dp[i - one][0] + dp[i - one][1]) % 1000000007
            if i >= low:
                sum += (dp[i][0] + dp[i][1])
                sum %= 1000000007
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.countGoodStrings(2, 3, 1, 2) == 5)
    print(s.countGoodStrings(3, 3, 1, 1) == 8)

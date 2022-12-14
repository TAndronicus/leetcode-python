from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if k >= length / 2:
            res = 0
            for i in range(1, length):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        dp = [[0] * length for _ in range(k + 1)]
        for i in range(1, k + 1):
            tmpMax = -prices[0]
            for j in range(1, length):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmpMax)
                tmpMax = max(tmpMax, dp[i - 1][j] - prices[j])
        return dp[k][length - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(2, [2, 4, 1]) == 2)
    print(s.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7)
    a = 0b11000000
    b = 0b11010101
    print(a & b == 0b11000000)
    print(a & b)

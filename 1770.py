from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(i + 1):
                if i == j:
                    dp[i][j] = dp[i - 1][j - 1] + nums[j - 1] * multipliers[i - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + nums[n - i] * multipliers[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j - 1] + nums[j - 1] * multipliers[i - 1], dp[i - 1][j] + nums[n + j - i] * multipliers[i - 1])
        return max(dp[m])


if __name__ == '__main__':
    s = Solution()
    print(s.maximumScore([1, 2, 3], [3, 2, 1]) == 14)
    print(s.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]) == 102)

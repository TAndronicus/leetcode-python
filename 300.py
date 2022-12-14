from typing import List


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        srt = sorted(set(nums))
        return self.needlemanWunsch(nums, srt)

    def needlemanWunsch(self, left: List[int], right: List[int]):
        dp = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]
        for i in range(len(left)):
            for j in range(len(right)):
                if left[i] == right[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[len(left)][len(right)]

    def lengthOfLIS2(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS1([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
    print(s.lengthOfLIS1([0, 1, 0, 3, 2, 3]) == 4)
    print(s.lengthOfLIS1([7, 7, 7, 7, 7, 7, 7]) == 1)
    print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
    print(s.lengthOfLIS2([0, 1, 0, 3, 2, 3]) == 4)
    print(s.lengthOfLIS2([7, 7, 7, 7, 7, 7, 7]) == 1)
    print(s.lengthOfLIS2([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6)

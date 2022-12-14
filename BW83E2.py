from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        consecutiveZeros, sum = 0, 0
        for el in nums:
            if el == 0:
                consecutiveZeros += 1
            else:
                sum += consecutiveZeros * (consecutiveZeros + 1) / 2
                consecutiveZeros = 0
        sum += consecutiveZeros * (consecutiveZeros + 1) / 2
        return int(sum)


if __name__ == '__main__':
    s = Solution()
    print(s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6)
    print(s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9)
    print(s.zeroFilledSubarray([2, 10, 2019]) == 0)
    print(s.zeroFilledSubarray([0, 2, 0, 10, 0, 2019]) == 3)

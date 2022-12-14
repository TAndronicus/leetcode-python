import math


class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        for i in range(int(n / 2) + 1):
            sum += math.comb(n - i, i)
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(1) == 1)
    print(s.climbStairs(2) == 2)
    print(s.climbStairs(3) == 3)
    print(s.climbStairs(4) == 5)
    print(s.climbStairs(5) == 8)
    print(s.climbStairs(6) == 13)

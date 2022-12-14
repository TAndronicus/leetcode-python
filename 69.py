import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        current, jump = int(x / 2), math.ceil(x / 4)
        while True:
            if current * current <= x and (current + 1) * (current + 1) > x:
                return current
            elif current * current > x:
                current -= jump
                jump = math.ceil(jump / 2)
            else:
                current += jump
                jump = math.ceil(jump / 2)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(0) == 0)
    print(s.mySqrt(1) == 1)
    print(s.mySqrt(2) == 1)
    print(s.mySqrt(3) == 1)
    print(s.mySqrt(4) == 2)
    print(s.mySqrt(5) == 2)
    print(s.mySqrt(6) == 2)
    print(s.mySqrt(7) == 2)
    print(s.mySqrt(8) == 2)
    print(s.mySqrt(9) == 3)
    print(s.mySqrt(10) == 3)
    print(s.mySqrt(11) == 3)

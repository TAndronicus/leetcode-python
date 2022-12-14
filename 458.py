import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest / minutesToDie + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.poorPigs(1000, 15, 60) == 5)
    print(s.poorPigs(4, 15, 15) == 2)
    print(s.poorPigs(4, 15, 30) == 2)

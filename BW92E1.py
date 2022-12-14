class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 1:
            return n
        else:
            return int(n / 2)


if __name__ == '__main__':
    s = Solution()

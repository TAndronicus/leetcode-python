class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(0b00000000000000000000000000001011) == 3)
    print(s.hammingWeight(0b00000000000000000000000010000000) == 1)
    print(s.hammingWeight(0b11111111111111111111111111111101) == 31)

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(0b00000010100101000001111010011100) == 964176192)
    print(s.reverseBits(0b11111111111111111111111111111101) == 3221225471)

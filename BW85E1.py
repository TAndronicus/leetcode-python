class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        index, sum = k, 0
        for i in range(k):
            if (blocks[i] == 'B'):
                sum += 1
        maximum = sum
        while index < len(blocks):
            if blocks[index - k] != blocks[index]:
                if blocks[index] == 'B':
                    sum += 1
                else:
                    sum -= 1
            maximum = max(maximum, sum)
            if maximum == k:
                return 0
            index += 1
        return max(k - maximum, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumRecolors("WBBWWBBWBW", 7) == 3)
    print(s.minimumRecolors("WBWBBBW", 2) == 0)

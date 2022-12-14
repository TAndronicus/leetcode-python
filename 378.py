from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        queued = [0] * length
        for i in range(k):
            lowestIndexes = [length - 1, length - 1]
            lowest = matrix[lowestIndexes[0]][lowestIndexes[1]]
            for row in range(min(i + 1, length)):
                if queued[row] < length and matrix[row][queued[row]] < lowest:
                    lowest = matrix[row][queued[row]]
                    lowestIndexes = [row, queued[row]]
            queued[lowestIndexes[0]] += 1
        return lowest


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
    print(s.kthSmallest([[-5]], 1) == -5)

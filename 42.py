from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        leftIndex, rightIndex = 0, len(height) - 1
        leftValue, rightValue = height[leftIndex], height[rightIndex]
        trapped, currentTrapHeight = 0, min(leftValue, rightValue)
        while leftIndex < rightIndex:
            if leftValue <= rightValue:
                leftIndex += 1
                leftValue = height[leftIndex]
                if leftValue > currentTrapHeight:
                    currentTrapHeight = min(leftValue, rightValue)
                else:
                    trapped += currentTrapHeight - leftValue
            else:
                rightIndex -= 1
                rightValue = height[rightIndex]
                if rightValue > currentTrapHeight:
                    currentTrapHeight = min(leftValue, rightValue)
                else:
                    trapped += currentTrapHeight - rightValue
        return trapped


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
    print(s.trap([4, 2, 0, 3, 2, 5]) == 9)
    print(s.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]) == 83)

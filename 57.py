from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        elif newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        left, right = 0, len(intervals) - 1
        while True:
            if intervals[left][1] >= newInterval[0]:
                break
            left += 1
        while True:
            if intervals[right][0] <= newInterval[1]:
                break
            right -= 1
        return intervals[:left] + [[min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]] + intervals[right + 1:]


if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1, 2], [3, 4]], [-1, 0]) == [[-1, 0], [1, 2], [3, 4]])
    print(s.insert([[1, 2], [3, 4]], [5, 6]) == [[1, 2], [3, 4], [5, 6]])
    print(s.insert([[1, 2], [3, 4]], [2, 3]) == [[1, 4]])
    print(s.insert([[1, 2], [3, 4]], [4, 5]) == [[1, 2], [3, 5]])
    print(s.insert([[1, 2], [3, 4], [5, 6]], [3, 4]) == [[1, 2], [3, 4], [5, 6]])
    print(s.insert([[1, 2], [3, 4], [5, 6], [7, 8]], [4, 5]) == [[1, 2], [3, 6], [7, 8]])
    print(s.insert([[1, 2], [3, 4], [5, 6], [7, 8]], [3, 5]) == [[1, 2], [3, 6], [7, 8]])
    print(s.insert([[1, 2], [3, 4], [5, 6], [7, 8]], [4, 6]) == [[1, 2], [3, 6], [7, 8]])
    print(s.insert([[1, 2], [3, 4], [5, 6], [7, 8]], [3, 6]) == [[1, 2], [3, 6], [7, 8]])
    print(s.insert([[1, 2], [3, 4], [5, 6], [7, 8]], [3, 7]) == [[1, 2], [3, 8]])
    print(s.insert([[1, 2], [3, 4], [7, 8]], [5, 6]) == [[1, 2], [3, 4], [5, 6], [7, 8]])
    print(s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
    print(s.insert([], [4, 8]) == [[4, 8]])

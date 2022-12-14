from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda el: (el[0], el[1]))
        res, current = [], intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= current[1]:
                current[1] = max(intervals[i][1], current[1])
            else:
                res.append(current)
                current = intervals[i]
        res.append(current)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
    print(s.merge([[1, 4], [4, 5]]) == [[1, 5]])
    print(s.merge([[1, 5]]) == [[1, 5]])

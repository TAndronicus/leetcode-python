class Solution:
    def bestClosingTime(self, customers: str) -> int:
        maxIndex, max, cumSum = 0, 0, 0
        for i, el in enumerate(customers):
            if el == 'Y':
                cumSum += 1
            else:
                cumSum -= 1
            if cumSum > max:
                maxIndex = i + 1
                max = cumSum
        return maxIndex


if __name__ == '__main__':
    s = Solution()
    print(s.bestClosingTime("YYNY"))
    print(s.bestClosingTime("NNNNN"))
    print(s.bestClosingTime("YYYY"))

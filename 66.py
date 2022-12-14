from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if all(i == 9 for i in digits):
            return [1] + ([0] * len(digits))
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry, incremented = True, True
            else:
                digits[i] += 1
                carry, incremented = False, True
            if incremented and not carry:
                break
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]) == [1, 2, 4])
    print(s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2])
    print(s.plusOne([9]) == [1, 0])
    print(s.plusOne([9, 9, 9]) == [1, 0, 0, 0])
    print(s.plusOne([8, 9, 9]) == [9, 0, 0])
    print(s.plusOne([8, 7, 9]) == [8, 8, 0])
    print(s.plusOne([0]) == [1])

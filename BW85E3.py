from typing import List


class Solution:
    A_INT = ord('a')
    MODULUS = ord('z') - A_INT + 1

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cumShifts = [0] * (len(s) + 1)
        for shift in shifts:
            if shift[2]:
                cumShifts[shift[0]] += 1
                cumShifts[shift[1] + 1] -= 1
            else:
                cumShifts[shift[0]] -= 1
                cumShifts[shift[1] + 1] += 1
        newStr = [''] * len(s)
        cumShift = 0
        for i in range(len(s)):
            cumShift += cumShifts[i]
            newNum = (ord(s[i]) - self.A_INT + cumShift)
            newModulus = newNum % self.MODULUS
            newStr[i] = chr(newModulus + self.A_INT)
        return ''.join(newStr)


if __name__ == '__main__':
    s = Solution()
    print(s.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace")
    print(s.shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz")

class Solution:
    def countAndSay(self, n: int) -> str:
        say = '1'
        while n > 1:
            newSay, currentChar, currentAmount = '', '', 0
            for c in say:
                if c != currentChar:
                    newSay = newSay + str(currentAmount) + currentChar
                    currentChar, currentAmount = c, 1
                else:
                    currentAmount = currentAmount + 1
            say = newSay[1:] + str(currentAmount) + currentChar
            n = n - 1
        return say


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1) == '1')
    print(s.countAndSay(4) == '1211')

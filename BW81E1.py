class Solution:
    def countAsterisks(self, s: str) -> int:
        betweenPairs, occurences = False, 0
        for c in s:
            if c == '|':
                betweenPairs = not betweenPairs
            elif c == '*' and not betweenPairs:
                occurences += 1
        return occurences


if __name__ == '__main__':
    s = Solution()
    print(s.countAsterisks("l|*e*et|c**o|*de|") == 2)
    print(s.countAsterisks("iamprogrammer") == 0)
    print(s.countAsterisks("yo|uar|e**|b|e***au|tifu|l") == 5)
    print(s.countAsterisks("yo|uar|e**|b|e***au|tifu|l") == 5)
    print(s.countAsterisks("*") == 1)
    print(s.countAsterisks("|*|") == 0)
    print(s.countAsterisks("|*|*") == 1)

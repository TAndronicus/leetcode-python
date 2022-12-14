class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        s, counter = s.rstrip(), 0
        for c in reversed(s):
            if c == ' ':
                return counter
            else:
                counter += 1
        return counter


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World") == 5)
    print(s.lengthOfLastWord("   fly me   to   the moon  ") == 4)
    print(s.lengthOfLastWord("luffy is still joyboy") == 6)
    print(s.lengthOfLastWord(" ") == 0)
    print(s.lengthOfLastWord2("Hello World") == 5)
    print(s.lengthOfLastWord2("   fly me   to   the moon  ") == 4)
    print(s.lengthOfLastWord2("luffy is still joyboy") == 6)
    print(s.lengthOfLastWord2(" ") == 0)

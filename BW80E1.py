class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        lowerCase, upperCase, digit, sign = False, False, False, False
        for c in password:
            if lowerCase and upperCase and digit and sign:
                break
            lowerCase = lowerCase or c.islower()
            upperCase = upperCase or c.isupper()
            digit = digit or c.isdigit()
            sign = sign or (c in '!@#$%^&*()-+')
        return lowerCase and upperCase and digit and sign


if __name__ == '__main__':
    s = Solution()
    print(s.strongPasswordCheckerII('IloveLe3tcode!'))
    print(not s.strongPasswordCheckerII('Me+You--IsMyDream'))
    print(not s.strongPasswordCheckerII('1aB!'))
    print(not s.strongPasswordCheckerII('abcd1234!'))
    print(not s.strongPasswordCheckerII('ABCD1234!'))
    print(not s.strongPasswordCheckerII('ABCDabcd!'))
    print(not s.strongPasswordCheckerII('ABCDabcd1'))
    print(not s.strongPasswordCheckerII('ABCDabcd11!'))
